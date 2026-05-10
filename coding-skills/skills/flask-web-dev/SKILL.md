---
name: flask-web-dev
description: |
  Flask web development best practices including routing, templates, database, auth, and error handling.
  Invoke when working on Flask (.py) backend projects.
version: "1.0.0"
author: "Trae Coding Skills Team"
license: MIT
---

# Flask Web 开发规范

专门针对 Flask 框架的后端开发最佳实践，涵盖路由设计、模板渲染、数据库操作、认证安全和错误处理。

## 自动触发条件

**强触发**：
- 文件后缀为 `.py` 且包含 `flask`、`Flask`、`@app` 关键词
- 用户提及 "Flask"、"后端"、"API"、"路由"
- 开发 Web 应用、REST API、模板渲染

**补充触发**（Karpathy 技能可调用）：
- 涉及数据库操作的 Python 代码
- 涉及用户认证、会话管理的场景
- 涉及文件上传、JSON API 开发的场景

## 核心规则

### 1. 项目结构规范

**推荐的 Flask 项目结构**：
```
project/
├── app.py              # 主应用入口
├── templates/          # HTML 模板
│   └── index.html
├── static/            # 静态文件
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt    # 依赖清单
└── instance/          # SQLite 数据库（如果使用）
```

**禁止**：
- ❌ 所有代码都写在 `app.py`（超过 500 行）
- ❌ 模板文件和 Python 文件混放
- ❌ 敏感信息硬编码在代码中

**推荐**：
- ✅ 使用 `blueprints` 组织大型应用
- ✅ 配置信息放在 `config.py` 或环境变量
- ✅ 数据库连接封装为独立模块

### 2. 路由设计规范

**基础路由**：
```python
# ✅ Good: RESTful 风格路由
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """获取课程列表"""
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses])

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """获取单个课程"""
    course = Course.query.get_or_404(course_id)
    return jsonify(course.to_dict())
```

**路由分组（蓝图）**：
```python
# ✅ Good: 使用蓝图组织路由
from flask import Blueprint
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/courses')
def get_courses():
    return jsonify([])

@api.route('/lessons/<int:lesson_id>')
def get_lesson(lesson_id):
    return jsonify({})
```

**禁止**：
- ❌ 路由中使用复杂业务逻辑
- ❌ 在路由中直接写 SQL 语句（应封装到模型层）

### 3. JSON API 响应规范

**统一响应格式**：
```python
from flask import jsonify

def success_response(data, message="Success", status_code=200):
    """统一成功响应格式"""
    return jsonify({
        'success': True,
        'message': message,
        'data': data
    }), status_code

def error_response(message, error_code=None, status_code=400):
    """统一错误响应格式"""
    response = {
        'success': False,
        'message': message
    }
    if error_code:
        response['error_code'] = error_code
    return jsonify(response), status_code

# 使用示例
@app.route('/api/courses/<int:course_id>')
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return error_response('课程不存在', 'NOT_FOUND', 404)
    return success_response(course.to_dict())
```

**API 版本控制**：
```python
# ✅ Good: URL 版本控制
@app.route('/api/v1/courses')  # v1 版本
@app.route('/api/v2/courses')  # v2 版本
```

### 4. 数据库操作规范

**使用上下文管理器**：
```python
# ✅ Good: 明确的连接管理
import sqlite3
from contextlib import contextmanager

DATABASE = 'instance/app.db'

@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

# 使用
with get_db() as conn:
    c = conn.cursor()
    c.execute('SELECT * FROM courses')
    courses = [dict(row) for row in c.fetchall()]
```

**禁止**：
- ❌ 全局变量持有数据库连接
- ❌ SQL 语句字符串拼接（存在注入风险）
- ❌ 不关闭数据库连接

**使用参数化查询**：
```python
# ✅ Good: 参数化查询防注入
c.execute('SELECT * FROM users WHERE email = ?', (email,))

# ❌ Bad: 字符串拼接
c.execute('SELECT * FROM users WHERE email = "' + email + '"')
```

### 5. 认证与会话安全

**密码处理**：
```python
import hashlib
import secrets

def hash_password(password, salt=None):
    """密码哈希 - 使用 SHA256 + salt"""
    if salt is None:
        salt = secrets.token_hex(16)
    hash_obj = hashlib.sha256((password + salt).encode())
    return salt + hash_obj.hexdigest()

def verify_password(password, hashed):
    """验证密码"""
    salt = hashed[:32]
    return hash_password(password, salt) == hashed

# 使用
hashed = hash_password('user_password')
if verify_password(input_password, stored_hash):
    # 登录成功
    session['user_id'] = user_id
```

**Session 安全配置**：
```python
from flask import Flask, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # 生产环境必须使用强随机密钥

# Session 配置
app.config.update(
    SESSION_COOKIE_SECURE=True,      # 仅 HTTPS 传输
    SESSION_COOKIE_HTTPONLY=True,    # 禁止 JavaScript 访问
    SESSION_COOKIE_SAMESITE='Lax',  # CSRF 防护
    PERMANENT_SESSION_LIFETIME=3600  # 1小时过期
)
```

**禁止**：
- ❌ 使用简单哈希或不哈希存储密码
- ❌ 在 URL 中传递认证 token
- ❌ Session 不设置过期时间

### 6. 错误处理规范

**全局错误处理器**：
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.error(f'Unhandled exception: {error}')
    return jsonify({'error': 'An unexpected error occurred'}), 500
```

**API 错误响应**：
```python
@app.route('/api/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    try:
        lesson = get_lesson_from_db(lesson_id)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404
        return jsonify(lesson), 200
    except DatabaseError as e:
        app.logger.error(f'Database error: {e}')
        return jsonify({'message': 'Database error'}), 500
```

### 7. 模板渲染规范

**模板路径**：
```python
# ✅ 模板放在 templates 目录
# Flask 会自动在 templates/ 目录下查找
@app.route('/')
def index():
    return render_template('index.html')

# ❌ 不要使用绝对路径
return render_template('/Users/name/project/templates/index.html')
```

**模板数据过滤**：
```python
# ✅ 传递数据前过滤敏感信息
def sanitize_user_data(user):
    return {
        'id': user['id'],
        'username': user['username'],
        # 不包含 password_hash, email 等敏感信息
    }

@app.route('/profile')
def profile():
    user = get_user(session['user_id'])
    return render_template('profile.html', user=sanitize_user_data(user))
```

## 强制检查清单

**代码提交前**：
1. [ ] 所有 SQL 查询使用参数化查询
2. [ ] 用户密码使用 hashlib 哈希存储
3. [ ] Session 配置了 `secret_key`
4. [ ] API 路由有认证检查（`if 'user_id' not in session`）
5. [ ] 敏感配置使用环境变量而非硬编码
6. [ ] 所有异常都被捕获或记录日志
7. [ ] 数据库连接正确关闭

**API 开发**：
1. [ ] 统一的成功/错误响应格式
2. [ ] 适当的 HTTP 状态码（200, 201, 400, 401, 404, 500）
3. [ ] CORS 配置正确（如果前后端分离）

## 场景化输出

### 【新 API 开发】
```
输出顺序：路由设计 → 请求参数校验 → 数据库操作 → 响应格式 → 错误处理
```

### 【修复安全漏洞】
```
输出顺序：漏洞定位 → 风险评估 → 修复方案 → 验证方法
```

## 与其他技能配合

- **universal-karpathy-coding-guidelines**: 整体编码原则指导
- **frontend-compatibility**: 前端代码兼容性检查

## 版本更新日志
- v1.0.0 - 初始版本，基于 Flask 官方最佳实践和常见安全规范