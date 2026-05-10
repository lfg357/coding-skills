---
name: frontend-compatibility
description: |
  Ensures frontend code (HTML/CSS/JS) is compatible across browsers.
  Invoke when modifying .html, .css, .js files or working on UI/interfaces.
version: "1.0.0"
author: "Trae Coding Skills Team"
license: MIT
---

# 前端兼容性检查

专门针对 HTML/CSS/JavaScript 代码的浏览器兼容性问题检测和处理。

## 自动触发条件

**强触发**（满足任一条件即启用）：
- 文件后缀为 `.html`, `.css`, `.js`
- 用户提及"前端"、"界面"、"交互"、"浏览器兼容"
- 进行 UI 功能开发、DOM 操作、事件处理

**弱触发**（Karpathy 技能可补充调用）：
- Flask 项目中 templates 目录下的文件
- 任何包含 HTML/CSS/JS 代码的上下文

## 核心规则

### 1. JavaScript ES6+ 语法兼容性检查

**禁止使用的语法**（除非确认目标环境支持）：
```javascript
// ❌ 可选链操作符 - IE11 及部分旧版浏览器不支持
const value = obj?.property?.nested;

// ✅ 替代方案
const value = obj && obj.property && obj.property.nested;

// ❌ 空值合并运算符 - 部分浏览器不支持
const result = value ?? 'default';

// ✅ 替代方案
const result = value !== null && value !== undefined ? value : 'default';

// ❌ 逻辑空赋值 -= 部分浏览器不支持
x ??= 'default';

// ✅ 替代方案
if (x === null || x === undefined) x = 'default';
```

**模板字符串兼容性处理**：
```javascript
// ✅ 模板字符串 - 现代浏览器都支持，但避免嵌套复杂逻辑
const html = '<div>' + item.name + '</div>';

// ❌ 如果必须使用模板字符串，避免以下模式
const html = `<div class="${item.matched ? 'active' : ''}">${getName()}</div>`;

// ✅ 简化版本 - 兼容性更好
var className = 'match-item';
if (item.matched) className += ' matched';
var div = '<div class="' + className + '">' + item.text + '</div>';
```

### 2. DOM 和事件处理兼容性

**事件对象处理**：
```javascript
// ❌ 可能的问题代码
element.addEventListener('click', (event) => {
    event?.target?.classList.add('active');
});

// ✅ 兼容版本
element.addEventListener('click', function(e) {
    var target = e.target || e.srcElement;
    if (target) {
        target.classList.add('active');
    }
});

// ✅ 或者使用事件委托
element.addEventListener('click', function(e) {
    var target = e.target || e.srcElement;
    if (target && target.classList.contains('match-item')) {
        // 处理逻辑
    }
});
```

**可选参数默认值处理**：
```javascript
// ❌ 问题代码
function showSection(sectionId, eventObj = null) {
    eventObj?.target?.classList.add('active');
}

// ✅ 兼容版本
function showSection(sectionId, eventObj) {
    var sections = ['home', 'courses'];
    // 基础逻辑

    if (eventObj && eventObj.target) {
        eventObj.target.classList.add('active');
    }
}
```

### 3. CSS 兼容性

**Flexbox 和 Grid**：
```css
/* ✅ 现代 Flexbox - iOS Safari 7+, Android Browser 4.4+ 支持 */
.container {
    display: -webkit-flex;  /* iOS 6, Safari 3.1-6 */
    display: flex;
}

/* ✅ CSS Grid - IE不支持，需要回退方案 */
.grid {
    display: -ms-grid;  /* IE 10 */
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}
```

**CSS 变量**：
```css
/* ✅ CSS 变量 - IE不支持 */
:root {
    --primary-color: #667eea;
}

/* ✅ 回退方案 */
.btn {
    background: #667eea;  /* IE 回退值 */
    background: var(--primary-color, #667eea);  /* 现代浏览器 */
}
```

### 4. Fetch API 和 Promise 兼容性

```javascript
// ❌ Fetch API - IE完全不支持
fetch('/api/data')
    .then(response => response.json())
    .catch(error => console.error(error));

// ✅ 兼容版本 - 需要 polyfill 或 XMLHttpRequest
// 方案1: 添加 polyfill
// <script src="https://cdn.jsdelivr.net/npm/whatwg-fetch@3.6.2/fetch.min.js"></script>

// 方案2: 使用 XMLHttpRequest
function apiCall(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            callback(null, JSON.parse(xhr.responseText));
        } else {
            callback(new Error('HTTP ' + xhr.status));
        }
    };
    xhr.onerror = function() {
        callback(new Error('Network error'));
    };
    xhr.send();
}
```

## 强制检查清单

**JavaScript 代码修改前**：
1. [ ] 检查是否使用了 `?.` 可选链操作符 → 替换为 `&&` 链式调用
2. [ ] 检查是否使用了 `??` 空值合并 → 替换为三元运算符
3. [ ] 检查 `event?.target` 模式 → 替换为 `if (event && event.target)`
4. [ ] 检查模板字符串中的复杂表达式 → 简化为字符串拼接
5. [ ] 检查 `classList.contains()` 兼容性 → 现代浏览器都支持，无需修改

**CSS 代码修改前**：
1. [ ] 检查是否使用了 `var()` CSS 变量 → 添加回退值
2. [ ] 检查 `display: grid` → 确认不需要支持 IE
3. [ ] 检查 `position: sticky` → iOS Safari 7.1+ 才支持

## 场景化输出

### 【新前端功能开发】
```
输出顺序：兼容性检查 → 备选方案 → 建议实现 → 验证方法
```

### 【修复浏览器兼容性问题】
```
输出顺序：问题定位 → 根因分析 → 修复方案 → 测试建议
```

## 与其他技能配合

- **universal-karpathy-coding-guidelines**: 极简编码原则
- **hybrid-python-web**: 前后端协作协调

## 版本更新日志
- v1.0.0 - 初始版本，整合 Web 开发中的常见兼容性问题