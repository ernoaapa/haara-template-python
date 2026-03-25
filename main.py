from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI(title="My Python App")

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Python App</title>
  <style>
    :root {
      --bg: #09090b; --surface: #18181b; --surface-2: #27272a;
      --border: #3f3f46; --text: #fafafa; --text-muted: #a1a1aa;
      --accent: #6ee7b7;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    header {
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      backdrop-filter: blur(16px);
      background: rgba(9,9,11,.8);
      position: sticky; top: 0; z-index: 10;
    }
    .logo { font-weight: 700; font-size: 1rem; color: var(--accent); }
    .badge {
      font-size: 0.75rem; padding: 3px 10px;
      background: var(--surface-2); border: 1px solid var(--border);
      border-radius: 999px; color: var(--text-muted);
    }
    main { flex: 1; max-width: 900px; margin: 0 auto; padding: 64px 24px; width: 100%; }
    .hero { margin-bottom: 56px; }
    .hero-tag {
      display: inline-block; margin-bottom: 16px;
      padding: 4px 12px; border-radius: 999px; font-size: 0.8rem;
      background: rgba(110,231,183,.1); border: 1px solid rgba(110,231,183,.3);
      color: var(--accent);
    }
    h1 {
      font-size: clamp(2rem, 5vw, 3rem); font-weight: 800;
      letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 16px;
    }
    .highlight {
      background: linear-gradient(135deg, #6ee7b7, #34d399);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    .lead { color: var(--text-muted); font-size: 1rem; line-height: 1.7; max-width: 540px; margin-bottom: 28px; }
    .endpoint-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 56px; }
    .endpoint-card {
      background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
      padding: 18px 20px; transition: border-color .15s, transform .15s; text-decoration: none; color: inherit;
      display: block;
    }
    .endpoint-card:hover { border-color: var(--text-muted); transform: translateY(-2px); }
    .endpoint-method {
      display: inline-block; font-size: 0.72rem; font-weight: 700;
      padding: 2px 8px; border-radius: 4px; margin-bottom: 8px;
      background: rgba(110,231,183,.12); color: var(--accent); border: 1px solid rgba(110,231,183,.25);
    }
    .endpoint-path { font-family: ui-monospace, monospace; font-size: 0.88rem; margin-bottom: 6px; }
    .endpoint-desc { font-size: 0.82rem; color: var(--text-muted); }
    .api-box {
      background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
      overflow: hidden;
    }
    .api-box-head {
      padding: 12px 18px; border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
      background: rgba(255,255,255,.02);
    }
    .api-box-title { font-size: 0.85rem; font-weight: 600; }
    .api-box-sub { font-size: 0.78rem; color: var(--text-muted); }
    .api-box-body { padding: 18px 20px; }
    pre {
      font-family: ui-monospace, monospace; font-size: 0.82rem;
      color: var(--accent); white-space: pre-wrap; word-break: break-all;
    }
    footer {
      border-top: 1px solid var(--border); padding: 20px 24px;
      text-align: center; font-size: 0.82rem; color: var(--text-muted);
    }
  </style>
</head>
<body>
  <header>
    <span class="logo">🐍 MyApp</span>
    <span class="badge">FastAPI + Python 3.12</span>
  </header>
  <main>
    <section class="hero">
      <div class="hero-tag">Template ✦</div>
      <h1>Python API,<br><span class="highlight">up and running</span></h1>
      <p class="lead">
        A FastAPI starter with automatic docs, hot reload, and production-ready structure.
        Edit <code>main.py</code> to start building your API.
      </p>
    </section>

    <h2 style="font-size:1rem;font-weight:600;color:var(--text-muted);margin-bottom:16px;letter-spacing:.04em;text-transform:uppercase;">
      Available endpoints
    </h2>
    <div class="endpoint-grid">
      <a class="endpoint-card" href="/">
        <span class="endpoint-method">GET</span>
        <div class="endpoint-path">/</div>
        <div class="endpoint-desc">This page — HTML response from FastAPI.</div>
      </a>
      <a class="endpoint-card" href="/api/hello">
        <span class="endpoint-method">GET</span>
        <div class="endpoint-path">/api/hello</div>
        <div class="endpoint-desc">JSON greeting. Add your own routes here.</div>
      </a>
      <a class="endpoint-card" href="/docs">
        <span class="endpoint-method">GET</span>
        <div class="endpoint-path">/docs</div>
        <div class="endpoint-desc">Interactive Swagger UI, auto-generated from your code.</div>
      </a>
      <a class="endpoint-card" href="/redoc">
        <span class="endpoint-method">GET</span>
        <div class="endpoint-path">/redoc</div>
        <div class="endpoint-desc">ReDoc API reference documentation.</div>
      </a>
    </div>

    <div class="api-box">
      <div class="api-box-head">
        <span class="api-box-title">Try the API</span>
        <span class="api-box-sub">GET /api/hello</span>
      </div>
      <div class="api-box-body">
        <pre id="json-output">Loading…</pre>
      </div>
    </div>
  </main>
  <footer>Built with FastAPI &amp; Uvicorn · <a href="/docs" style="color:var(--text-muted)">API docs</a></footer>
  <script>
    fetch('/api/hello')
      .then(r => r.json())
      .then(d => document.getElementById('json-output').textContent = JSON.stringify(d, null, 2))
      .catch(() => document.getElementById('json-output').textContent = 'Could not fetch /api/hello');
  </script>
  <script>
    (function() {
      var proto = location.protocol === 'https:' ? 'wss:' : 'ws:';
      function connect() {
        var ws = new WebSocket(proto + '//' + location.host + '/ws/reload');
        ws.onclose = function() {
          setTimeout(function() {
            var s = new WebSocket(proto + '//' + location.host + '/ws/reload');
            s.onopen = function() { location.reload(); };
            s.onclose = function() { connect(); };
          }, 1000);
        };
      }
      connect();
    })();
  </script>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML


@app.get("/api/hello")
async def hello():
    return {
        "message": "Hello from FastAPI!",
        "framework": "FastAPI",
        "python": "3.12",
        "docs": "/docs",
    }


@app.websocket("/ws/reload")
async def reload_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        pass


@app.get("/api/items/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    """Fetch a single item by ID, with optional query filter."""
    return {"item_id": item_id, "query": q}
