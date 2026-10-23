/**
 * Kronos V15.2: High-Fidelity Quant Trading Workstation (Option A)
 * 60 FPS Client-Side Multi-Pane Canvas Engine powered by TradingView Lightweight Charts
 */

(function (window) {
  'use strict';

  class QuantWorkstation {
    constructor(containerId, options = {}) {
      this.container = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
      if (!this.container) {
        console.error(`QuantWorkstation: container #${containerId} not found.`);
        return;
      }

      this.options = Object.assign({
        theme: 'dark',
        height: 850,
      }, options);

      this.charts = {};
      this.series = {};
      this.payload = null;
      this.activeEventIndex = -1;
      this.layerVisibility = {
        candles: true,
        donchian: true,
        shelf: true,
        stop: true,
        ema200: true,
        markers: true
      };

      this.initLayout();
    }

    $(id) {
      return this.container.querySelector('#' + id);
    }

    initLayout() {
      this.container.innerHTML = `
        <div class="workstation-container">
          <!-- Loading Overlay -->
          <div class="workstation-loading" id="kw-loading-overlay" style="display:none; position:absolute; inset:0; background:rgba(9,13,20,0.85); z-index:50; flex-direction:column; align-items:center; justify-content:center; backdrop-filter:blur(4px);">
            <div class="kw-spinner" style="width:40px; height:40px; border:3px solid rgba(0,240,255,0.2); border-top-color:#00f0ff; border-radius:50%; animation:kw-spin 0.8s linear infinite;"></div>
            <div id="kw-loading-msg" style="margin-top:12px; font-size:13px; color:#00f0ff; font-weight:600; font-family:monospace;">Loading Shard...</div>
          </div>

          <!-- Top Control Ribbon -->
          <div class="workstation-ribbon" id="kw-ribbon">
            <div class="workstation-ribbon-left">
              <div class="workstation-symbol-badge">
                <span id="kw-sym-title">---</span>
                <span class="workstation-tier-tag" id="kw-sym-tier">TIER 1</span>
              </div>
              <div class="workstation-quick-stats">
                <div class="workstation-stat-item">
                  <span class="workstation-stat-label">Last Price</span>
                  <span class="workstation-stat-val" id="kw-stat-price">--</span>
                </div>
                <div class="workstation-stat-item">
                  <span class="workstation-stat-label">24h Chg</span>
                  <span class="workstation-stat-val" id="kw-stat-chg">--</span>
                </div>
                <div class="workstation-stat-item">
                  <span class="workstation-stat-label">24h Vol</span>
                  <span class="workstation-stat-val" id="kw-stat-vol">--</span>
                </div>
                <div class="workstation-stat-item">
                  <span class="workstation-stat-label">Open Interest</span>
                  <span class="workstation-stat-val" id="kw-stat-oi">--</span>
                </div>
                <div class="workstation-stat-item">
                  <span class="workstation-stat-label">Whale L/S</span>
                  <span class="workstation-stat-val" id="kw-stat-ls">--</span>
                </div>
                <div class="workstation-stat-item">
                  <span class="workstation-stat-label">Funding APR</span>
                  <span class="workstation-stat-val" id="kw-stat-funding">--</span>
                </div>
              </div>
            </div>

            <div class="workstation-ribbon-right">
              <!-- Pane Jump Navigator -->
              <div class="workstation-btn-group" title="Scroll directly to pane">
                <button class="workstation-btn-pill active" id="btn-scroll-price">📊 Candles</button>
                <button class="workstation-btn-pill" id="btn-scroll-vol">📦 Volume</button>
                <button class="workstation-btn-pill" id="btn-scroll-oi" style="color:#38bdf8; font-weight:700;">🐋 Open Interest & L/S</button>
                <button class="workstation-btn-pill" id="btn-scroll-funding" style="color:#00f0ff;">⚡ Funding</button>
              </div>

              <!-- Quick Timeframe Navigator -->
              <div class="workstation-btn-group">
                <button class="workstation-btn-pill" data-range="7">7D</button>
                <button class="workstation-btn-pill" data-range="14">14D</button>
                <button class="workstation-btn-pill active" data-range="30">30D</button>
                <button class="workstation-btn-pill" data-range="60">60D</button>
                <button class="workstation-btn-pill" data-range="all">ALL</button>
              </div>

              <!-- Layer Toggles -->
              <button class="workstation-layer-btn active" id="btn-toggle-donchian" title="Donchian 14d Floor">
                <span class="layer-dot" style="background:#00f0ff;"></span> Floor
              </button>
              <button class="workstation-layer-btn active" id="btn-toggle-shelf" title="72h Compression Shelf">
                <span class="layer-dot" style="background:#d946ef;"></span> Shelf
              </button>
              <button class="workstation-layer-btn active" id="btn-toggle-stop" title="Resting Stop Line">
                <span class="layer-dot" style="background:#8b5cf6;"></span> Stop
              </button>
              <button class="workstation-layer-btn active" id="btn-toggle-ema" title="200d Macro EMA">
                <span class="layer-dot" style="background:#f59e0b;"></span> 200d
              </button>
              <button class="workstation-layer-btn active" id="btn-toggle-markers" title="Entry & Veto Markers">
                <span class="layer-dot" style="background:#00ff87;"></span> Signals
              </button>
            </div>
          </div>

          <!-- Split Viewport: 4-Pane Chart & Signal Inspector -->
          <div class="workstation-body">
            <!-- Left Chart Panes with Vertical Scroller -->
            <div class="workstation-panes" id="kw-panes-box">
              <!-- Pane 1: Main Price & Overlays (500px) -->
              <div class="pane-wrapper" id="pane-price">
                <div class="main-pane-legend" id="kw-live-legend">
                  <div class="legend-item"><span class="legend-key">O:</span><span class="legend-val" id="leg-open">--</span></div>
                  <div class="legend-item"><span class="legend-key">H:</span><span class="legend-val" id="leg-high">--</span></div>
                  <div class="legend-item"><span class="legend-key">L:</span><span class="legend-val" id="leg-low">--</span></div>
                  <div class="legend-item"><span class="legend-key">C:</span><span class="legend-val" id="leg-close">--</span></div>
                  <div class="legend-item"><span class="legend-key">Vol:</span><span class="legend-val" id="leg-vol">--</span></div>
                </div>
              </div>

              <!-- Pane 2: Volume Histogram (160px) -->
              <div class="pane-wrapper" id="pane-volume">
                <div class="pane-label">
                  <span>VOLUME</span>
                  <span class="pane-metric-val" id="leg-sub-vol">--</span>
                </div>
              </div>

              <!-- Pane 3: Open Interest & Top Trader L/S (280px) -->
              <div class="pane-wrapper" id="pane-oi">
                <div class="pane-label">
                  <span>OPEN INTEREST & WHALE L/S</span>
                  <span class="pane-metric-val" id="leg-sub-oi" style="color: #38bdf8;">--</span>
                  <span class="pane-metric-val" id="leg-sub-ls" style="color: #f59e0b; margin-left: 10px;">--</span>
                </div>
              </div>

              <!-- Pane 4: Funding Rate Histogram (200px) -->
              <div class="pane-wrapper" id="pane-funding">
                <div class="pane-label">
                  <span>FUNDING RATE (APR)</span>
                  <span class="pane-metric-val" id="leg-sub-funding">--</span>
                </div>
              </div>
            </div>

            <!-- Right Signal Inspector Sidebar -->
            <div class="workstation-sidebar" id="kw-sidebar">
              <div class="inspector-header">
                <div class="inspector-title">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                  </svg>
                  <span>Signal Inspector</span>
                </div>
                <div class="inspector-timestamp" id="insp-timestamp">--</div>
              </div>

              <div class="inspector-body">
                <!-- Causal Decision Banner -->
                <div class="decision-banner neutral" id="insp-banner">
                  <span id="insp-banner-text">Hover or select a bar</span>
                </div>

                <!-- Strategy Conditions Checklist -->
                <div class="inspector-card">
                  <div class="inspector-card-title">
                    <span>Strategy Conditions</span>
                    <span style="font-size: 10px; color: var(--kw-text-faint);">Causal Bar t</span>
                  </div>
                  <div class="condition-list" id="insp-conditions-list">
                    <div style="font-size: 11px; color: var(--kw-text-faint); text-align: center; padding: 10px;">
                      Move crosshair over candlesticks to audit bar-by-bar decision logic
                    </div>
                  </div>
                </div>

                <!-- Active Risk & Position Card -->
                <div class="inspector-card" id="insp-risk-card" style="display: none;">
                  <div class="inspector-card-title">
                    <span>Active Risk Profile</span>
                    <span id="insp-risk-book" style="color: var(--kw-neon-cyan);">Book</span>
                  </div>
                  <div class="metric-grid">
                    <div class="metric-cell">
                      <span class="metric-cell-label">Entry Price</span>
                      <span class="metric-cell-val" id="insp-risk-entry">--</span>
                    </div>
                    <div class="metric-cell">
                      <span class="metric-cell-label">Stop Level</span>
                      <span class="metric-cell-val" id="insp-risk-stop" style="color: var(--kw-neon-magenta);">--</span>
                    </div>
                    <div class="metric-cell">
                      <span class="metric-cell-label">Dist to Stop</span>
                      <span class="metric-cell-val" id="insp-risk-dist">--</span>
                    </div>
                    <div class="metric-cell">
                      <span class="metric-cell-label">MTM PnL</span>
                      <span class="metric-cell-val" id="insp-risk-pnl" style="color: var(--kw-neon-green);">--</span>
                    </div>
                  </div>
                </div>

                <!-- Veto Rationale Card -->
                <div class="inspector-card" id="insp-veto-card" style="display: none; border-color: rgba(255, 70, 85, 0.4);">
                  <div class="inspector-card-title" style="color: var(--kw-neon-red);">
                    <span>Veto Flight Telemetry</span>
                    <span id="insp-veto-badge" class="status-badge fail">Blocked</span>
                  </div>
                  <div class="condition-row" style="background: rgba(255, 70, 85, 0.08);">
                    <span class="condition-name">Veto Gate:</span>
                    <span class="condition-val" id="insp-veto-gate" style="color: #ffffff;">--</span>
                  </div>
                  <div class="condition-row">
                    <span class="condition-name">Candidate Setup:</span>
                    <span class="condition-val" id="insp-veto-setup">--</span>
                  </div>
                  <div class="metric-grid" style="margin-top: 4px;">
                    <div class="metric-cell">
                      <span class="metric-cell-label">Dodged Bullet?</span>
                      <span class="metric-cell-val" id="insp-veto-dodged">--</span>
                    </div>
                    <div class="metric-cell">
                      <span class="metric-cell-label">72h Forward MFE</span>
                      <span class="metric-cell-val" id="insp-veto-mfe">--</span>
                    </div>
                  </div>
                </div>

                <!-- OHLCV & Derivatives Card -->
                <div class="inspector-card">
                  <div class="inspector-card-title">Bar Anatomy</div>
                  <div class="metric-grid">
                    <div class="metric-cell">
                      <span class="metric-cell-label">Close</span>
                      <span class="metric-cell-val" id="insp-bar-close">--</span>
                    </div>
                    <div class="metric-cell">
                      <span class="metric-cell-label">Volume</span>
                      <span class="metric-cell-val" id="insp-bar-vol">--</span>
                    </div>
                    <div class="metric-cell">
                      <span class="metric-cell-label">Token OI</span>
                      <span class="metric-cell-val" id="insp-bar-oi">--</span>
                    </div>
                    <div class="metric-cell">
                      <span class="metric-cell-label">Funding APR</span>
                      <span class="metric-cell-val" id="insp-bar-funding">--</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Event Jump Navigation Bar -->
              <div class="event-navigator-bar">
                <button class="event-nav-btn" id="btn-prev-event">
                  &#9664; Prev Event
                </button>
                <div style="font-size: 11px; color: var(--kw-text-faint); align-self: center;" id="event-counter-text">
                  0 / 0
                </div>
                <button class="event-nav-btn" id="btn-next-event">
                  Next Event &#9654;
                </button>
              </div>
            </div>
          </div>
        </div>
      `;

      this.bindButtons();
    }

    bindButtons() {
      // Timeframe buttons
      const tfButtons = this.container.querySelectorAll('.workstation-btn-pill');
      tfButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
          tfButtons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          const range = btn.dataset.range;
          this.applyTimeRange(range);
        });
      });

      // Quick Pane Scroll Jump buttons
      const scrollToPane = (paneId) => {
        const pEl = this.$(paneId);
        if (pEl) {
          pEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      };

      if (this.$('btn-scroll-price')) {
        this.$('btn-scroll-price').addEventListener('click', () => scrollToPane('pane-price'));
      }
      if (this.$('btn-scroll-vol')) {
        this.$('btn-scroll-vol').addEventListener('click', () => scrollToPane('pane-volume'));
      }
      if (this.$('btn-scroll-oi')) {
        this.$('btn-scroll-oi').addEventListener('click', () => scrollToPane('pane-oi'));
      }
      if (this.$('btn-scroll-funding')) {
        this.$('btn-scroll-funding').addEventListener('click', () => scrollToPane('pane-funding'));
      }

      // Layer toggle buttons
      const toggleLayer = (btnId, key, seriesName) => {
        const btn = this.$(btnId);
        if (!btn) return;
        btn.addEventListener('click', () => {
          this.layerVisibility[key] = !this.layerVisibility[key];
          btn.classList.toggle('active', this.layerVisibility[key]);
          if (seriesName && this.series[seriesName]) {
            this.series[seriesName].applyOptions({
              visible: this.layerVisibility[key]
            });
          }
          if (key === 'markers') {
            this.toggleMarkers(this.layerVisibility[key]);
          }
        });
      };

      toggleLayer('btn-toggle-donchian', 'donchian', 'donchianFloor');
      toggleLayer('btn-toggle-shelf', 'shelf', 'compressionShelf');
      toggleLayer('btn-toggle-stop', 'stop', 'restingStop');
      toggleLayer('btn-toggle-ema', 'ema200', 'ema200');
      toggleLayer('btn-toggle-markers', 'markers', null);

      // Event traversal buttons
      const btnPrev = this.$('btn-prev-event');
      const btnNext = this.$('btn-next-event');

      if (btnPrev) {
        btnPrev.addEventListener('click', () => this.navigateEvent(-1));
      }
      if (btnNext) {
        btnNext.addEventListener('click', () => this.navigateEvent(1));
      }

      // Keyboard shortcuts
      window.addEventListener('keydown', (e) => {
        if (!this.container || !this.payload) return;
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;

        if (e.key === 'ArrowLeft') {
          this.navigateEvent(-1);
        } else if (e.key === 'ArrowRight') {
          this.navigateEvent(1);
        } else if (e.key === 'Home') {
          this.scrollToLatest();
        }
      });
    }

    showLoading(show, msg = '') {
      const overlay = this.$('kw-loading-overlay');
      const msgEl = this.$('kw-loading-msg');
      if (!overlay) return;
      if (show) {
        overlay.style.display = 'flex';
        if (msgEl && msg) msgEl.textContent = msg;
      } else {
        overlay.style.display = 'none';
      }
    }

    async loadSymbol(symbol, bars = 2500) {
      try {
        this.showLoading(true, `Loading ${symbol} Shard & Causal Signals...`);
        const res = await fetch(`/api/workstation/${encodeURIComponent(symbol)}?bars=${bars}`);
        if (!res.ok) {
          throw new Error(`HTTP ${res.status}: Failed to fetch ${symbol}`);
        }
        const data = await res.json();
        this.render(data);
      } catch (err) {
        console.error('Workstation error:', err);
        this.showLoading(true, `Error loading ${symbol}: ${err.message}`);
        setTimeout(() => this.showLoading(false), 3000);
      } finally {
        this.showLoading(false);
      }
    }

    render(payload) {
      this.payload = payload;
      this.updateHeaderSummary(payload.summary);

      // Clean up previous charts if any
      this.destroyCharts();

      const commonChartOptions = {
        layout: {
          background: { color: '#090d14' },
          textColor: '#94a3b8',
          fontSize: 11,
          fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace',
        },
        grid: {
          vertLines: { color: 'rgba(30, 41, 59, 0.5)' },
          horzLines: { color: 'rgba(30, 41, 59, 0.5)' },
        },
        crosshair: {
          mode: LightweightCharts.CrosshairMode.Normal,
          vertLine: {
            color: '#64748b',
            width: 1,
            style: LightweightCharts.LineStyle.Dashed,
            labelBackgroundColor: '#1e293b',
          },
          horzLine: {
            color: '#64748b',
            width: 1,
            style: LightweightCharts.LineStyle.Dashed,
            labelBackgroundColor: '#1e293b',
          },
        },
        timeScale: {
          borderColor: '#1e293b',
          timeVisible: true,
          secondsVisible: false,
        },
        rightPriceScale: {
          borderColor: '#1e293b',
          autoScale: true,
          scaleMargins: { top: 0.1, bottom: 0.1 },
        },
        handleScroll: { mouseWheel: false, pressedMouseMove: true, horzTouchDrag: true },
        handleScale: { axisPressedMouseMove: true, mouseWheel: true, pinch: true },
      };

      // 1. Chart Pane 1: Main Price & Overlays (500px)
      const p1El = this.$('pane-price');
      this.charts.price = LightweightCharts.createChart(p1El, {
        ...commonChartOptions,
        height: 500,
      });

      // Main Candlestick series
      this.series.candles = this.charts.price.addCandlestickSeries({
        upColor: '#00ff87',
        downColor: '#ff4655',
        borderUpColor: '#00ff87',
        borderDownColor: '#ff4655',
        wickUpColor: '#00ff87',
        wickDownColor: '#ff4655',
      });
      this.series.candles.setData(payload.candles);

      // Donchian 14d Floor (Cyan Step-line)
      this.series.donchianFloor = this.charts.price.addLineSeries({
        color: '#00f0ff',
        lineWidth: 2,
        lineType: LightweightCharts.LineType.WithSteps,
        title: 'Floor',
        priceLineVisible: false,
        lastValueVisible: false,
      });
      this.series.donchianFloor.setData(payload.donchian_floor || []);

      // 72h Compression Shelf (Fuchsia Step-line)
      this.series.compressionShelf = this.charts.price.addLineSeries({
        color: '#d946ef',
        lineWidth: 2,
        lineType: LightweightCharts.LineType.WithSteps,
        title: 'Shelf',
        priceLineVisible: false,
        lastValueVisible: false,
      });
      this.series.compressionShelf.setData(payload.compression_shelf || []);

      // Resting Stop Line (Purple Step-line)
      this.series.restingStop = this.charts.price.addLineSeries({
        color: '#8b5cf6',
        lineWidth: 2,
        lineType: LightweightCharts.LineType.WithSteps,
        title: 'Stop',
        priceLineVisible: false,
        lastValueVisible: false,
      });
      this.series.restingStop.setData(payload.resting_stop || []);

      // 200d Macro EMA Line (Amber Smooth line)
      this.series.ema200 = this.charts.price.addLineSeries({
        color: '#f59e0b',
        lineWidth: 1,
        lineType: LightweightCharts.LineType.Simple,
        title: 'EMA 200d',
        priceLineVisible: false,
        lastValueVisible: false,
      });
      this.series.ema200.setData(payload.ema200 || []);

      // Set Entry, Exit, and Veto Markers
      this.allMarkers = payload.markers || [];
      if (this.layerVisibility.markers) {
        this.series.candles.setMarkers(this.allMarkers);
      }

      // 2. Chart Pane 2: Volume Histogram (160px)
      const p2El = this.$('pane-volume');
      this.charts.volume = LightweightCharts.createChart(p2El, {
        ...commonChartOptions,
        height: 160,
        timeScale: { ...commonChartOptions.timeScale, visible: false },
      });
      this.series.volume = this.charts.volume.addHistogramSeries({
        priceFormat: { type: 'volume' },
        priceScaleId: '',
        scaleMargins: { top: 0.2, bottom: 0 },
      });
      this.series.volume.setData(payload.volume);

      // 3. Chart Pane 3: Open Interest & Top Trader L/S (280px Roomy Display)
      const p3El = this.$('pane-oi');
      this.charts.oi = LightweightCharts.createChart(p3El, {
        ...commonChartOptions,
        height: 280,
        timeScale: { ...commonChartOptions.timeScale, visible: false },
        leftPriceScale: {
          visible: true,
          borderColor: '#1e293b',
          scaleMargins: { top: 0.1, bottom: 0.1 },
        },
      });

      // Token Open Interest Spline Area
      this.series.oi = this.charts.oi.addAreaSeries({
        topColor: 'rgba(56, 189, 248, 0.4)',
        bottomColor: 'rgba(56, 189, 248, 0.02)',
        lineColor: '#38bdf8',
        lineWidth: 2,
        priceScaleId: 'right',
      });
      this.series.oi.setData(payload.open_interest || []);

      // Top Trader Long/Short Ratio Line (Left Price Scale)
      this.series.ls = this.charts.oi.addLineSeries({
        color: '#f59e0b',
        lineWidth: 2,
        priceScaleId: 'left',
        title: 'L/S',
      });
      this.series.ls.setData(payload.toptrader_ls || []);

      // 4. Chart Pane 4: Funding Rate Histogram (200px)
      const p4El = this.$('pane-funding');
      this.charts.funding = LightweightCharts.createChart(p4El, {
        ...commonChartOptions,
        height: 200,
      });
      this.series.funding = this.charts.funding.addHistogramSeries({
        priceFormat: { type: 'custom', formatter: (val) => `${(val * 100).toFixed(4)}%` },
        scaleMargins: { top: 0.15, bottom: 0.15 },
      });
      this.series.funding.setData(payload.funding_rate || []);

      // Synchronize All 4 Panes in Lockstep
      this.syncPanes();

      // Subscribe Unified Crosshair Move Events
      this.setupCrosshairSync();

      // Setup Responsive Resize Observer
      this.setupResize();

      // Set initial 30D range
      this.applyTimeRange('30');

      // Update event counter in sidebar
      this.updateEventCounter();

      // Load latest candle into inspector by default
      if (payload.candles.length > 0) {
        const lastCandle = payload.candles[payload.candles.length - 1];
        this.updateInspector(lastCandle.time);
      }

      // Force canvas expansion to full flex width
      setTimeout(() => this.resizeAll(), 50);
      setTimeout(() => this.resizeAll(), 250);
    }

    syncPanes() {
      const chartList = [this.charts.price, this.charts.volume, this.charts.oi, this.charts.funding];
      let isSyncing = false;

      chartList.forEach((srcChart) => {
        srcChart.timeScale().subscribeVisibleLogicalRangeChange((range) => {
          if (isSyncing || !range) return;
          isSyncing = true;
          chartList.forEach((tgtChart) => {
            if (tgtChart !== srcChart) {
              tgtChart.timeScale().setVisibleLogicalRange(range);
            }
          });
          isSyncing = false;
        });
      });
    }

    setupCrosshairSync() {
      const chartList = [
        { chart: this.charts.price, name: 'price' },
        { chart: this.charts.volume, name: 'volume' },
        { chart: this.charts.oi, name: 'oi' },
        { chart: this.charts.funding, name: 'funding' },
      ];

      chartList.forEach(({ chart }) => {
        chart.subscribeCrosshairMove((param) => {
          if (!param || !param.time) {
            return;
          }

          const tSec = typeof param.time === 'object' ? param.time.timestamp : param.time;
          this.updateInspector(tSec);
          this.updateLegend(param);
        });
      });
    }

    updateLegend(param) {
      if (!param || !param.time || !this.series.candles) return;
      const data = param.seriesData.get(this.series.candles);
      if (!data) return;

      const formatP = (v) => v !== undefined && v !== null ? `$${v}` : '--';
      if (this.$('leg-open')) this.$('leg-open').textContent = formatP(data.open);
      if (this.$('leg-high')) this.$('leg-high').textContent = formatP(data.high);
      if (this.$('leg-low')) this.$('leg-low').textContent = formatP(data.low);
      if (this.$('leg-close')) this.$('leg-close').textContent = formatP(data.close);

      // Volume in legend
      const volData = param.seriesData.get(this.series.volume);
      if (volData) {
        const volStr = volData.value !== undefined ? Number(volData.value).toLocaleString() : '--';
        if (this.$('leg-vol')) this.$('leg-vol').textContent = volStr;
        if (this.$('leg-sub-vol')) this.$('leg-sub-vol').textContent = volStr;
      }

      // OI and L/S in legend
      const oiData = param.seriesData.get(this.series.oi);
      if (oiData && oiData.value !== undefined) {
        if (this.$('leg-sub-oi')) this.$('leg-sub-oi').textContent = `OI: ${Number(oiData.value).toLocaleString()}`;
      }
      const lsData = param.seriesData.get(this.series.ls);
      if (lsData && lsData.value !== undefined) {
        if (this.$('leg-sub-ls')) this.$('leg-sub-ls').textContent = `L/S: ${Number(lsData.value).toFixed(2)}`;
      }

      // Funding in legend
      const fundData = param.seriesData.get(this.series.funding);
      if (fundData && fundData.value !== undefined) {
        const apr = fundData.value * 3 * 365 * 100;
        if (this.$('leg-sub-funding')) this.$('leg-sub-funding').textContent = `${(fundData.value * 100).toFixed(4)}% (${apr.toFixed(1)}% APR)`;
      }
    }

    updateInspector(tSec) {
      if (!this.payload || !this.payload.inspection_index) return;
      const state = this.payload.inspection_index[String(tSec)];
      if (!state) return;

      // Timestamp
      if (this.$('insp-timestamp')) this.$('insp-timestamp').textContent = state.timestamp_iso || '--';

      // Decision Banner
      const banner = this.$('insp-banner');
      const bannerText = this.$('insp-banner-text');
      if (banner && bannerText) {
        banner.className = `decision-banner ${state.banner.type}`;
        bannerText.textContent = state.banner.text;
      }

      // Conditions Checklist
      const condListEl = this.$('insp-conditions-list');
      if (condListEl) {
        if (state.conditions && state.conditions.length > 0) {
          condListEl.innerHTML = state.conditions.map(c => `
            <div class="condition-row">
              <div class="condition-name" title="${c.desc || ''}">
                <span class="status-badge ${c.status}">${c.status}</span>
                <span>${c.name}</span>
              </div>
              <div class="condition-val">${c.value}</div>
            </div>
          `).join('');
        } else {
          condListEl.innerHTML = `<div style="font-size:11px;color:var(--kw-text-faint);padding:6px;">No conditions evaluated</div>`;
        }
      }

      // Risk Card
      const riskCard = this.$('insp-risk-card');
      if (riskCard) {
        if (state.risk && state.risk.entry_price) {
          riskCard.style.display = 'flex';
          if (this.$('insp-risk-book')) this.$('insp-risk-book').textContent = state.risk.book || 'Book';
          if (this.$('insp-risk-entry')) this.$('insp-risk-entry').textContent = state.risk.entry_price;
          if (this.$('insp-risk-stop')) this.$('insp-risk-stop').textContent = state.risk.current_stop || '--';
          if (this.$('insp-risk-dist')) this.$('insp-risk-dist').textContent = state.risk.dist_to_stop || '--';
          if (this.$('insp-risk-pnl')) this.$('insp-risk-pnl').textContent = state.risk.pnl_mtm || '--';
        } else {
          riskCard.style.display = 'none';
        }
      }

      // Veto Card
      const vetoCard = this.$('insp-veto-card');
      if (vetoCard) {
        if (state.veto && state.veto.gate) {
          vetoCard.style.display = 'flex';
          if (this.$('insp-veto-gate')) this.$('insp-veto-gate').textContent = state.veto.gate;
          if (this.$('insp-veto-setup')) this.$('insp-veto-setup').textContent = state.veto.setup;
          if (this.$('insp-veto-dodged')) this.$('insp-veto-dodged').textContent = state.veto.is_dodged ? 'YES (Profitable Veto)' : 'NO';
          if (this.$('insp-veto-mfe')) this.$('insp-veto-mfe').textContent = state.veto.mfe_72h || '--';
        } else {
          vetoCard.style.display = 'none';
        }
      }

      // Bar Anatomy Card
      if (state.ohlcv) {
        if (this.$('insp-bar-close')) this.$('insp-bar-close').textContent = state.ohlcv.close;
        if (this.$('insp-bar-vol')) this.$('insp-bar-vol').textContent = state.ohlcv.volume;
        if (this.$('insp-bar-oi')) this.$('insp-bar-oi').textContent = state.ohlcv.oi;
        if (this.$('insp-bar-funding')) this.$('insp-bar-funding').textContent = state.ohlcv.funding;
      }
    }

    updateHeaderSummary(summary) {
      if (!summary) return;
      if (this.$('kw-sym-title')) this.$('kw-sym-title').textContent = summary.symbol || '---';
      if (this.$('kw-sym-tier')) this.$('kw-sym-tier').textContent = summary.tier || 'TIER 1';
      if (this.$('kw-stat-price')) this.$('kw-stat-price').textContent = summary.last_price || '--';

      const chgEl = this.$('kw-stat-chg');
      if (chgEl) {
        chgEl.textContent = summary.chg_24h || '--';
        chgEl.style.color = (summary.chg_24h_val >= 0) ? '#00ff87' : '#ff4655';
      }

      if (this.$('kw-stat-vol')) this.$('kw-stat-vol').textContent = summary.vol_24h || '--';
      if (this.$('kw-stat-oi')) this.$('kw-stat-oi').textContent = summary.open_interest || '--';
      if (this.$('kw-stat-ls')) this.$('kw-stat-ls').textContent = summary.ls_ratio || '--';
      if (this.$('kw-stat-funding')) this.$('kw-stat-funding').textContent = summary.funding_apr || '--';
    }

    applyTimeRange(rangeDays) {
      if (!this.charts.price || !this.payload || !this.payload.candles.length) return;
      const candles = this.payload.candles;
      const lastTime = candles[candles.length - 1].time;

      if (rangeDays === 'all') {
        this.charts.price.timeScale().fitContent();
        return;
      }

      const days = parseInt(rangeDays, 10);
      const fromTime = lastTime - (days * 86400);
      this.charts.price.timeScale().setVisibleRange({
        from: fromTime,
        to: lastTime,
      });
    }

    toggleMarkers(visible) {
      if (!this.series.candles) return;
      if (visible) {
        this.series.candles.setMarkers(this.allMarkers || []);
      } else {
        this.series.candles.setMarkers([]);
      }
    }

    navigateEvent(direction) {
      if (!this.payload || !this.payload.events || this.payload.events.length === 0) return;
      const events = this.payload.events;

      this.activeEventIndex += direction;
      if (this.activeEventIndex < 0) {
        this.activeEventIndex = events.length - 1;
      } else if (this.activeEventIndex >= events.length) {
        this.activeEventIndex = 0;
      }

      const event = events[this.activeEventIndex];
      this.jumpToTime(event.time);
      this.updateEventCounter();
    }

    jumpToTime(tSec) {
      if (!this.charts.price) return;
      // Center the viewport on the event timestamp with a 7-day window
      const halfWindow = 3.5 * 86400;
      this.charts.price.timeScale().setVisibleRange({
        from: tSec - halfWindow,
        to: tSec + halfWindow,
      });
      this.updateInspector(tSec);
    }

    scrollToLatest() {
      if (!this.charts.price) return;
      this.charts.price.timeScale().scrollToRealTime();
    }

    updateEventCounter() {
      const counterEl = this.$('event-counter-text');
      if (!counterEl) return;
      const total = this.payload && this.payload.events ? this.payload.events.length : 0;
      const current = total > 0 ? (this.activeEventIndex + 1) : 0;
      counterEl.textContent = `${current} / ${total} Events`;
    }

    resizeAll() {
      const p1El = this.$('pane-price');
      const p2El = this.$('pane-volume');
      const p3El = this.$('pane-oi');
      const p4El = this.$('pane-funding');
      const panesBox = this.$('kw-panes-box');

      const targetWidth = (panesBox && panesBox.clientWidth > 50) 
        ? panesBox.clientWidth 
        : (this.container ? Math.max(300, this.container.clientWidth - 360) : 0);

      if (targetWidth > 50) {
        if (this.charts.price && p1El) this.charts.price.resize(targetWidth, 500);
        if (this.charts.volume && p2El) this.charts.volume.resize(targetWidth, 160);
        if (this.charts.oi && p3El) this.charts.oi.resize(targetWidth, 280);
        if (this.charts.funding && p4El) this.charts.funding.resize(targetWidth, 200);
      }
    }

    setupResize() {
      const resizeCharts = () => this.resizeAll();

      window.addEventListener('resize', resizeCharts);

      const observer = new ResizeObserver(() => resizeCharts());
      const panesBox = this.$('kw-panes-box');
      if (panesBox) observer.observe(panesBox);
      if (this.container) observer.observe(this.container);

      // Multiple staggered passes to catch dynamic CSS grid/flex reflows
      setTimeout(resizeCharts, 50);
      setTimeout(resizeCharts, 200);
      setTimeout(resizeCharts, 500);
    }

    destroyCharts() {
      Object.keys(this.charts).forEach(key => {
        try {
          if (this.charts[key]) this.charts[key].remove();
        } catch (e) {
          // ignore
        }
      });
      this.charts = {};
      this.series = {};
    }
  }

  // Export to global window scope
  window.QuantWorkstation = QuantWorkstation;

})(window);
