<!DOCTYPE html>

<html lang="zh-CN">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>🌤️ 全球天气查询 · Global Weather Explorer</title>

<style>

* { margin: 0; padding: 0; box-sizing: border-box; }

body {

font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",

"Hiragino Sans GB", "Microsoft YaHei", sans-serif;

min-height: 100vh;

background: linear-gradient(160deg, #1e3a5f, #2d5f8f, #5b9bd5);

background-attachment: fixed;

color: #fff;

}

header { padding: 40px 24px 20px; text-align: center; }

header h1 {

font-size: 2.2rem;

font-weight: 700;

letter-spacing: 1px;

text-shadow: 0 2px 20px rgba(0,0,0,0.3);

}

header p { margin-top: 8px; color: rgba(255,255,255,0.8); font-size: 0.95rem; }

 

.container {

max-width: 900px;

margin: 0 auto;

padding: 0 20px 60px;

}

 

/* 搜索区 */

.search-bar {

display: flex;

gap: 10px;

margin-bottom: 24px;

flex-wrap: wrap;

}

.search-bar input {

flex: 1;

min-width: 200px;

padding: 14px 20px;

border-radius: 28px;

border: none;

background: rgba(255,255,255,0.2);

backdrop-filter: blur(12px);

color: #fff;

font-size: 1rem;

outline: none;

transition: 0.3s;

}

.search-bar input::placeholder { color: rgba(255,255,255,0.7); }

.search-bar input:focus { background: rgba(255,255,255,0.3); }

.search-bar button {

padding: 14px 28px;

border-radius: 28px;

border: none;

background: rgba(255,255,255,0.9);

color: #1e3a5f;

font-weight: 600;

font-size: 1rem;

cursor: pointer;

transition: 0.25s;

}

.search-bar button:hover { background: #fff; transform: scale(1.03); }

 

/* 快捷按钮 */

.quick-buttons {

display: flex;

flex-wrap: wrap;

gap: 8px;

margin-bottom: 30px;

justify-content: center;

}

.quick-btn {

padding: 8px 16px;

border-radius: 20px;

border: 1px solid rgba(255,255,255,0.35);

background: rgba(255,255,255,0.12);

color: #fff;

font-size: 0.85rem;

cursor: pointer;

backdrop-filter: blur(8px);

transition: 0.25s;

}

.quick-btn:hover { background: rgba(255,255,255,0.28); transform: translateY(-2px); }

 

/* 结果区域 */

.result { display: none; }

.result.show { display: block; }

 

.current {

background: rgba(255,255,255,0.15);

backdrop-filter: blur(16px);

border-radius: 24px;

padding: 36px;

margin-bottom: 24px;

border: 1px solid rgba(255,255,255,0.25);

text-align: center;

box-shadow: 0 10px 40px rgba(0,0,0,0.2);

}

.current .loc { font-size: 1.6rem; font-weight: 600; margin-bottom: 4px; }

.current .loc-sub { font-size: 0.9rem; color: rgba(255,255,255,0.8); margin-bottom: 20px; }

.current .temp { font-size: 5rem; font-weight: 200; line-height: 1; margin-bottom: 10px; }

.current .desc { font-size: 1.2rem; margin-bottom: 24px; }

 

.current-details {

display: grid;

grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));

gap: 14px;

text-align: left;

}

.current-details .item {

background: rgba(255,255,255,0.12);

border-radius: 14px;

padding: 12px 16px;

}

.current-details .label { font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-bottom: 4px; }

.current-details .val { font-size: 1.05rem; font-weight: 600; }

 

/* 7天预报 */

.forecast-title {

font-size: 1.1rem;

margin-bottom: 12px;

opacity: 0.9;

}

.forecast {

display: grid;

grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));

gap: 10px;

background: rgba(255,255,255,0.12);

backdrop-filter: blur(12px);

border-radius: 20px;

padding: 18px;

border: 1px solid rgba(255,255,255,0.2);

}

.day-card {

text-align: center;

padding: 14px 6px;

border-radius: 14px;

transition: 0.2s;

}

.day-card:hover { background: rgba(255,255,255,0.15); }

.day-card .day { font-size: 0.8rem; opacity: 0.85; margin-bottom: 6px; }

.day-card .ico { font-size: 2rem; margin-bottom: 4px; }

.day-card .hi { font-weight: 600; font-size: 1rem; }

.day-card .lo { font-size: 0.85rem; opacity: 0.7; margin-left: 4px; }

 

.loading, .empty, .error {

text-align: center;

padding: 40px;

color: rgba(255,255,255,0.85);

}

.spinner {

width: 40px; height: 40px;

border: 3px solid rgba(255,255,255,0.3);

border-top-color: #fff;

border-radius: 50%;

animation: spin 0.8s linear infinite;

margin: 0 auto 12px;

}

@keyframes spin { to { transform: rotate(360deg); } }

 

.suggestions {

background: rgba(255,255,255,0.95);

color: #1e3a5f;

border-radius: 14px;

margin-top: 6px;

overflow: hidden;

position: absolute;

width: calc(100% - 40px);

max-width: calc(100% - 40px);

z-index: 10;

box-shadow: 0 10px 30px rgba(0,0,0,0.2);

}

.suggestion-item {

padding: 10px 18px;

cursor: pointer;

font-size: 0.9rem;

border-bottom: 1px solid #eee;

}

.suggestion-item:last-child { border-bottom: none; }

.suggestion-item:hover { background: #e8f0f8; }

.suggestion-item .cname { font-weight: 600; }

.suggestion-item .ctry { font-size: 0.75rem; color: #666; margin-left: 6px; }

.search-wrap { position: relative; flex: 1; min-width: 200px; }

 

@media (max-width: 500px) {

header h1 { font-size: 1.6rem; }

.current { padding: 24px 20px; }

.current .temp { font-size: 4rem; }

}

</style>

</head>

<body>

 

<header>

<h1>🌤️ 全球天气查询</h1>

<p>Worldwide Weather Explorer · 实时天气 + 7 天预报</p>

</header>

 

<div class="container">

<div class="search-bar">

<div class="search-wrap">

<input type="text" id="cityInput" placeholder="输入城市名，如：北京 / Tokyo / 纽约..." autocomplete="off">

<div class="suggestions" id="suggestions" style="display:none;"></div>

</div>

<button id="searchBtn">🔍 查询天气</button>

</div>

 

<div class="quick-buttons" id="quickBtns"></div>

 

<div id="statusArea"></div>

 

<div class="result" id="result">

<div class="current" id="currentBox"></div>

<div class="forecast-title">📅 未来 7 天预报</div>

<div class="forecast" id="forecastBox"></div>

</div>

</div>

 

<script>

// ========= 天气代码映射 =========

const WMO = {

0: { desc: "晴", icon: "☀️" },

1: { desc: "大部晴朗", icon: "🌤️" },

2: { desc: "多云", icon: "⛅" },

3: { desc: "阴天", icon: "☁️" },

45: { desc: "雾", icon: "🌫️" },

48: { desc: "冻雾", icon: "🌫️" },

51: { desc: "小毛毛雨", icon: "🌦️" },

53: { desc: "中毛毛雨", icon: "🌦️" },

55: { desc: "大毛毛雨", icon: "🌧️" },

56: { desc: "冻毛毛雨", icon: "🌧️" },

57: { desc: "大冻毛毛雨", icon: "🌧️" },

61: { desc: "小雨", icon: "🌦️" },

63: { desc: "中雨", icon: "🌧️" },

65: { desc: "大雨", icon: "🌧️" },

66: { desc: "冻雨", icon: "🌧️❄️" },

67: { desc: "大冻雨", icon: "🌧️❄️" },

71: { desc: "小雪", icon: "🌨️" },

73: { desc: "中雪", icon: "❄️" },

75: { desc: "大雪", icon: "❄️" },

77: { desc: "雪粒", icon: "🌨️" },

80: { desc: "阵雨", icon: "🌦️" },

81: { desc: "中阵雨", icon: "🌧️" },

82: { desc: "大阵雨", icon: "⛈️" },

85: { desc: "阵雪", icon: "🌨️" },

86: { desc: "大阵雪", icon: "❄️" },

95: { desc: "雷暴", icon: "⛈️" },

96: { desc: "雷暴伴冰雹", icon: "⛈️" },

99: { desc: "强雷暴伴冰雹", icon: "⛈️" }

};

function weatherInfo(code) {

return WMO[code] || { desc: "未知", icon: "❓" };

}

 

// ========= 热门城市预设 =========

const QUICK_CITIES = [

{ name: "北京", lat: 39.9042, lon: 116.4074, country: "中国" },

{ name: "上海", lat: 31.2304, lon: 121.4737, country: "中国" },

{ name: "东京", lat: 35.6762, lon: 139.6503, country: "日本" },

{ name: "纽约", lat: 40.7128, lon: -74.0060, country: "美国" },

{ name: "伦敦", lat: 51.5074, lon: -0.1278, country: "英国" },

{ name: "巴黎", lat: 48.8566, lon: 2.3522, country: "法国" },

{ name: "迪拜", lat: 25.2048, lon: 55.2708, country: "阿联酋" },

{ name: "悉尼", lat: -33.8688, lon: 151.2093, country: "澳大利亚" },

{ name: "莫斯科", lat: 55.7558, lon: 37.6173, country: "俄罗斯" },

{ name: "里约热内卢", lat: -22.9068, lon: -43.1729, country: "巴西" }

];

 

// ========= DOM =========

const input = document.getElementById('cityInput');

const btn = document.getElementById('searchBtn');

const suggestions = document.getElementById('suggestions');

const statusArea = document.getElementById('statusArea');

const resultBox = document.getElementById('result');

const currentBox = document.getElementById('currentBox');

const forecastBox = document.getElementById('forecastBox');

 

// 渲染快捷按钮

const quickBtns = document.getElementById('quickBtns');

QUICK_CITIES.forEach(c => {

const b = document.createElement('button');

b.className = 'quick-btn';

b.textContent = `${c.name} (${c.country})`;

b.onclick = () => fetchWeather(c);

quickBtns.appendChild(b);

});

 

// ========= 地理编码（搜索建议）=========

let suggestTimer;

input.addEventListener('input', () => {

clearTimeout(suggestTimer);

const kw = input.value.trim();

if (kw.length < 1) { suggestions.style.display = 'none'; return; }

suggestTimer = setTimeout(async () => {

try {

const res = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(kw)}&count=5&language=zh&format=json`);

const data = await res.json();

if (!data.results || data.results.length === 0) {

suggestions.style.display = 'none';

return;

}

suggestions.innerHTML = data.results.map(r =>

`<div class="suggestion-item" data-lat="${r.latitude}" data-lon="${r.longitude}" data-name="${r.name}" data-country="${r.country || ''}">

<span class="cname">${r.name}</span><span class="ctry">${r.admin1 || ''} · ${r.country || ''}</span>

</div>`

).join('');

suggestions.style.display = 'block';

suggestions.querySelectorAll('.suggestion-item').forEach(item => {

item.addEventListener('click', () => {

const city = {

name: item.dataset.name,

lat: parseFloat(item.dataset.lat),

lon: parseFloat(item.dataset.lon),

country: item.dataset.country

};

suggestions.style.display = 'none';

input.value = city.name;

fetchWeather(city);

});

});

} catch (e) { suggestions.style.display = 'none'; }

}, 300);

});

 

document.addEventListener('click', (e) => {

if (!e.target.closest('.search-wrap')) suggestions.style.display = 'none';

});

 

btn.addEventListener('click', () => {

const kw = input.value.trim();

if (!kw) return;

// 如果是预设城市直接查

const preset = QUICK_CITIES.find(c => c.name === kw || c.nameEn === kw);

if (preset) { fetchWeather(preset); return; }

// 否则走地理编码

geocodeAndFetch(kw);

});

 

input.addEventListener('keydown', (e) => {

if (e.key === 'Enter') btn.click();

});

 

async function geocodeAndFetch(kw) {

showLoading();

try {

const res = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(kw)}&count=1&language=zh&format=json`);

const data = await res.json();

if (!data.results || data.results.length === 0) {

showError("未找到该城市，请尝试更准确的名称。");

return;

}

const r = data.results[0];

fetchWeather({ name: r.name, lat: r.latitude, lon: r.longitude, country: r.country || '' });

} catch (e) {

showError("网络请求失败，请稍后再试。");

}

}

 

// ========= 获取天气 =========

async function fetchWeather(city) {

showLoading();

resultBox.classList.remove('show');

statusArea.innerHTML = '';

 

try {

const url = `https://api.open-meteo.com/v1/forecast?latitude=${city.lat}&longitude=${city.lon}` +

`&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m,wind_direction_10m,surface_pressure` +

`&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset` +

`&timezone=auto`;

 

const res = await fetch(url);

if (!res.ok) throw new Error("API error");

const data = await res.json();

renderWeather(city, data);

} catch (e) {

showError("获取天气失败：" + e.message);

}

}

 

// ========= 渲染 =========

function showLoading() {

statusArea.innerHTML = `<div class="loading"><div class="spinner"></div>正在查询天气...</div>`;

}

function showError(msg) {

statusArea.innerHTML = `<div class="error">❌ ${msg}</div>`;

}

 

function renderWeather(city, data) {

statusArea.innerHTML = '';

const cur = data.current;

const daily = data.daily;

const tz = data.timezone;

 

// 当前

const wi = weatherInfo(cur.weather_code);

const windDir = degToCompass(cur.wind_direction_10m);

currentBox.innerHTML = `

<div class="loc">${city.name}</div>

<div class="loc-sub">${city.country} · 时区 ${tz}</div>

<div style="font-size:6rem;">${wi.icon}</div>

<div class="temp">${cur.temperature_2m.toFixed(0)}°C</div>

<div class="desc">${wi.desc} · 体感 ${cur.apparent_temperature.toFixed(0)}°C</div>

<div class="current-details">

<div class="item"><div class="label">💧 湿度</div><div class="val">${cur.relative_humidity_2m}%</div></div>

<div class="item"><div class="label">🌬️ 风速</div><div class="val">${cur.wind_speed_10m} km/h</div></div>

<div class="item"><div class="label">🧭 风向</div><div class="val">${windDir}</div></div>

<div class="item"><div class="label">📊 气压</div><div class="val">${cur.surface_pressure.toFixed(0)} hPa</div></div>

<div class="item"><div class="label">🌅 日出</div><div class="val">${formatTime(daily.sunrise[0])}</div></div>

<div class="item"><div class="label">🌇 日落</div><div class="val">${formatTime(daily.sunset[0])}</div></div>

</div>

`;

 

// 7天预报

const weekdays = ["周日","周一","周二","周三","周四","周五","周六"];

const today = new Date();

forecastBox.innerHTML = daily.time.map((dateStr, i) => {

const d = new Date(dateStr + "T00:00:00");

const dayLabel = i === 0 ? "今天" : weekdays[d.getDay()];

const wi2 = weatherInfo(daily.weather_code[i]);

const lo = daily.temperature_2m_min[i].toFixed(0);

const hi = daily.temperature_2m_max[i].toFixed(0);

const pop = daily.precipitation_probability_max[i];

return `

<div class="day-card">

<div class="day">${dayLabel}</div>

<div class="ico">${wi2.icon}</div>

<div class="hi">${hi}°<span class="lo">/${lo}°</span></div>

<div style="font-size:0.72rem;margin-top:4px;opacity:0.75;">💧${pop}%</div>

</div>

`;

}).join('');

 

resultBox.classList.add('show');

}

 

function degToCompass(deg) {

const dirs = ["北","东北","东","东南","南","西南","西","西北"];

return dirs[Math.round(deg / 45) % 8];

}

function formatTime(dtStr) {

const d = new Date(dtStr);

return d.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });

}

 

// 默认加载北京天气

fetchWeather(QUICK_CITIES[0]);

</script>

</body>

</html>
