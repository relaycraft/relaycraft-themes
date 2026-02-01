# 为 RelayCraft 主题做贡献

感谢你有兴趣为 RelayCraft 制作主题！🎨

## 🚀 创建主题

RelayCraft 中的主题是一个简单的文件夹结构，可以打包成 `.rctheme` (zip) 文件。

### 1. 最小结构（仅颜色）
对于简单的颜色自定义，你只需要一个 `theme.yaml` 文件。

**文件结构：**
```
my-theme/
└── theme.yaml
```

**theme.yaml:**
```yaml
id: "com.yourname.themes.my-theme"  # 唯一 ID（反向域名风格）
name: "My Cool Theme"
version: "1.0.0"
author: "Your Name"
type: "dark"  # 或 "light"
colors:
  # 基础 UI
  background: "#1e1e1e"
  foreground: "#d4d4d4"
  border: "#333333"
  
  # 品牌色
  primary: "#007acc"
  primary_foreground: "#ffffff"
  
  # 布局
  sidebar: "#252526"
  sidebar_foreground: "#f3f3f3"
  item_hover: "#2a2d2e"
  item_active: "#37373d"
```

### 2. 高级主题（CSS 与资源）
为了获得完全的控制权，你可以包含自定义 CSS 和本地资源（字体、图片）。

**文件结构：**
```
neon-dark/
├── theme.yaml
├── styles.css        # 自定义 CSS 注入
└── assets/           # 本地资源文件夹
    ├── background.png
    └── custom-font.woff2
```

**theme.yaml (高级):**
```yaml
id: "com.relaycraft.themes.neon-dark"
# ... 元数据 ...
css: "styles.css"  # 链接你的 CSS 文件
```

**styles.css (示例):**
```css
/* 从 assets/ 加载本地字体 */
@font-face {
  font-family: 'MyFont';
  src: url('assets/custom-font.woff2');
}

/* 应用于标题 */
h1, h2, h3 {
  font-family: 'MyFont', sans-serif !important;
  text-shadow: 0 0 10px #00ffcc;
}

/* 使用相对路径引用图片 */
.sidebar {
  background-image: url('assets/background.png');
}
```

## 📦 打包你的主题

1. 选中主题文件夹内的所有文件（`theme.yaml`, `styles.css`, `assets/`）。
2. 将它们压缩为 zip 包。
3. 将 `.zip` 扩展名重命名为 `.rctheme`（可选，但推荐）。
   - 例如：`my-theme.rctheme`

## 📮 提交到注册表

要让你的主题出现在 RelayCraft 的“市场”中，请按照以下步骤操作：

1. **Fork** 本仓库。
2. 将你的主题文件夹添加到 `themes/` 目录（可选，但有利于开源）。
3. 将你的 `.rctheme` 文件托管在可访问的地方（例如 GitHub Releases，或者如果你上传了源码，可以直接使用本仓库的 raw 文件链接）。
4. 编辑 `themes.json` 添加你的条目：

```json
{
  "id": "com.yourname.themes.my-theme",
  "name": "My Cool Theme",
  "version": "1.0.0",
  "description": "A brief description of your theme.",
  "author": "Your Name",
  "url": "https://github.com/.../releases/download/v1.0.0/my-theme.rctheme",
  "thumbnailUrl": "https://.../preview.png",
  "tags": ["dark", "purple", "cyberpunk"]
}
```

5. 提交 **Pull Request**。

## 🛠 测试

在提交之前，请在本地验证你的主题：
1. 打开 RelayCraft > 设置 > 外观。
2. 点击 "从文件安装 (Install from File)"。
3. 选择你的 `.rctheme` 文件。
4. 验证颜色、字体和资源是否正确加载。
