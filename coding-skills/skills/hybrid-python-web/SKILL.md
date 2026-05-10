---
name: hybrid-python-web
description: |
  Coordinates Python backend + HTML/JS frontend development.
  Invoke when working on Flask/FastAPI projects with frontend templates or serving static files.
version: "1.0.0"
author: "Trae Coding Skills Team"
license: MIT
---

# 混合 Python Web 开发指南

专门协调 Python 后端（Flask/FastAPI/Django）与 HTML/CSS/JS 前端的协同开发，解决上下文切换、API 设计、数据传递等问题。

## 自动触发条件

**强触发**：
- 项目同时包含 `.py` 后端文件和 `.html`/`.js` 前端文件
- 用户提及"前后端"、"API"、"模板"、"静态文件"
- 开发全栈 Web 应用（从数据库到界面）

**补充触发**（Karpathy 技能可调用）：
- 前后端数据交互场景
- 模板渲染与 JavaScript 交互
- CORS、认证token、session 共享

## 核心规则

### 1. 项目架构决策

**前后端分离 vs 模板渲染**：

```python
# 方案A: 完全前后端分离（推荐大型项目）
# 后端只提供 API
@app.route('/api/courses')
def get_courses():
    return jsonify(courses)

# 前端独立部署
# <script src="https://frontend.example.com/app.js">

# 方案B: Flask 模板渲染（中小型项目）
@app.route('/')
def index():
    return render_template('index.html')

# 方案C: API + 前端静态文件（混合 - 本项目采用）
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/<path:path>')
def api(path):
    return jsonify(handle_api(path))
```

**本项目选择方案C**，原因：
- 简单依赖（仅 Flask）
- 无需前端构建工具
- 便于快速迭代

### 2. API 设计协调

**前后端约定的 API 格式**：

```python
# ✅ 后端: 统一 JSON 响应
@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = load_courses()
    return jsonify(courses)  # 自动设置 Content-Type: application/json
```

```javascript
// ✅ 前端: fetch API 调用
async function loadCourses() {
    try {
        const response = await fetch('/api/courses');
        if (!response.ok) {
            throw new Error('HTTP ' + response.status);
        }
        const courses = await response.json();
        renderCourses(courses);
    } catch (error) {
        showError('加载失败: ' + error.message);
    }
}
```

**请求头配置**：
```python
# ✅ 后端: 允许跨域（如果前后端分离部署）
from flask_cors import CORS
CORS(app, supports_credentials=True)

# 或者手动设置
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response
```

```javascript
// ✅ 前端: 带凭证的请求（Cookie/Session）
const response = await fetch('/api/data', {
    credentials: 'include'  // 发送 Cookie
});
```

### 3. 数据传递模式

**场景1: 模板渲染传递数据**（方案B）
```python
# 后端
@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    stats = get_user_stats(user.id)
    return render_template('dashboard.html',
                          username=user.username,
                          stats=stats)
```

```html
<!-- 模板中直接使用 -->
<h1>欢迎, {{ username }}</h1>
<p>学习时长: {{ stats.hours }}小时</p>
```

**场景2: API 动态加载**（方案C - 本项目采用）
```python
# 后端
@app.route('/api/stats')
def get_stats():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    stats = get_user_stats(session['user_id'])
    return jsonify(stats)
```

```javascript
// 前端
async function loadStats() {
    const stats = await apiCall('/stats');
    document.getElementById('hours').textContent = stats.total_hours;
}
```

**禁止**：
- ❌ 模板中执行复杂 JavaScript 逻辑
- ❌ 后端直接返回 HTML 片段（应返回 JSON）
- ❌ 前端拼接 SQL 语句

### 4. 认证状态同步

**Session 认证流程**：
```python
# ✅ 后端: 登录时创建 session
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = verify_credentials(data['email'], data['password'])

    if user:
        session['user_id'] = user['id']  # Flask session
        session.permanent = True
        return jsonify({
            'success': True,
            'user': {'id': user['id'], 'username': user['username']}
        })
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
```

```javascript
// ✅ 前端: 登录后保存状态
async function handleLogin(credentials) {
    const result = await apiCall('/login', 'POST', credentials);

    if (result.success) {
        localStorage.setItem('user', JSON.stringify(result.user));
        updateUIForLoggedInUser(result.user);
        showFlash('登录成功', 'success');
    }
}
```

**状态检查**：
```python
# ✅ 后端: 所有需要认证的 API 检查 session
@app.route('/api/words/practice', methods=['POST'])
def practice_word():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    # 处理请求...
```

```javascript
// ✅ 前端: 调用前检查登录状态
async function startPractice() {
    if (!localStorage.getItem('user')) {
        showLoginPrompt();  // 引导用户登录
        return;
    }
    const words = await apiCall('/words');
    // 开始练习...
}
```

### 5. 错误处理协调

**后端错误响应**：
```python
# ✅ 统一错误格式
@app.route('/api/lessons/<int:lesson_id>')
def get_lesson(lesson_id):
    try:
        lesson = Lesson.query.get(lesson_id)
        if not lesson:
            return jsonify({'error': 'NOT_FOUND', 'message': '课时不存在'}), 404
        return jsonify(lesson.to_dict())

    except DatabaseError as e:
        app.logger.error(f'Database error for lesson {lesson_id}: {e}')
        return jsonify({'error': 'DB_ERROR', 'message': '数据库错误'}), 500

    except Exception as e:
        app.logger.error(f'Unexpected error: {e}')
        return jsonify({'error': 'INTERNAL_ERROR', 'message': '服务器错误'}), 500
```

**前端错误处理**：
```javascript
// ✅ 统一的 API 调用错误处理
async function apiCall(url, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include'  // 发送 session cookie
        };

        if (data) {
            options.body = JSON.stringify(data);
        }

        const response = await fetch('/api' + url, options);

        // 检查 HTTP 状态码
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || `HTTP ${response.status}`);
        }

        // 尝试解析 JSON
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return await response.json();
        }

        return await response.text();

    } catch (error) {
        console.error('API call failed:', url, error);
        showFlash('操作失败: ' + error.message, 'error');
        throw error;  // 重新抛出让调用方处理
    }
}

// ✅ 业务逻辑层错误处理
async function loadLessons() {
    try {
        showLoading();
        const lessons = await apiCall('/lessons');
        renderLessons(lessons);
    } catch (error) {
        // 不要在 catch 中重复 showFlash，apiCall 已处理
        renderEmptyState('暂无课时数据');
    } finally {
        hideLoading();
    }
}
```

### 6. 开发工作流

**文件结构**：
```
project/
├── app/                  # Flask 应用模块
│   ├── __init__.py       # 应用工厂
│   ├── routes.py          # 路由定义
│   ├── models.py          # 数据模型
│   ├── utils.py          # 工具函数
│   ├── errors.py         # 错误处理
│   ├── constants.py      # 常量定义
│   └── templates/        # 模板文件
│       └── index.html
├── instance/             # SQLite 数据库
│   └── language_learning.db
├── requirements.txt
└── run.py                # 应用入口
```

**调试技巧**：
```python
# ✅ 后端: 添加请求日志
import logging
logging.basicConfig(level=logging.DEBUG)

@app.before_request
def log_request():
    app.logger.debug(f'{request.method} {request.path}')

# ✅ 前端: API 调试
async function apiCall(url, method, data) {
    console.log(`API Call: ${method} ${url}`, data);
    const result = await actualFetch(...);
    console.log(`API Response: ${url}`, result);
    return result;
}
```

**热重载配置**：
```python
# Flask 开发模式自动重载
# 启动命令: flask run --debug
# 或代码中:
if __name__ == '__main__':
    app.debug = True  # 仅开发环境！
    app.run(host='0.0.0.0', port=5000)
```

## 强制检查清单

**前后端协作**：
1. [ ] API 响应格式统一（成功/错误）
2. [ ] 前端正确处理 401 未授权
3. [ ] Session/Cookie 认证配置 `credentials: 'include'`
4. [ ] 后端设置正确的 CORS 头（如果需要）
5. [ ] API 错误返回有意义的错误信息

**数据一致性**：
1. [ ] 前端显示的数据字段与后端 JSON key 一致
2. [ ] 类型一致（字符串 vs 数字 vs 布尔）
3. [ ] 空值处理（后端返回 `null` vs 前端期望 `[]`）

**用户体验**：
1. [ ] 加载状态显示（`showLoading()`/`hideLoading()`）
2. [ ] 错误提示（`showFlash(message, 'error')`）
3. [ ] 操作反馈（成功/失败/进行中）
4. [ ] 进度指示（百分比/步骤数）

## 常见问题解决方案

**Q: 前后端时间戳不一致？**
```python
# 后端返回 ISO 格式
from datetime import datetime
return jsonify({'created_at': datetime.now().isoformat()})
```

```javascript
// 前端解析
const date = new Date(data.created_at);
document.getElementById('time').textContent = date.toLocaleString();
```

**Q: 中文乱码？**
```python
# 后端设置 UTF-8
# Python 文件开头: # -*- coding: utf-8 -*-
# HTML 声明: <meta charset="UTF-8">

@app.route('/api/courses')
def get_courses():
    return jsonify(courses)  # Flask 自动处理 UTF-8
```

**Q: 文件上传大小限制？**
```python
# 后端配置
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({'error': 'File too large'}), 413
```

## 与其他技能配合

- **universal-karpathy-coding-guidelines**: 极简编码原则
- **flask-web-dev**: Flask 专项规范
- **frontend-compatibility**: 前端代码兼容性

## 版本更新日志
- v1.0.0 - 初始版本，整合前后端协作常见问题