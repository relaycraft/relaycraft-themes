# RelayCraft 主题仓库 🎨

**RelayCraft**（下一代 AI 驱动的 HTTP 客户端）的官方主题注册表。

本仓库托管了主题清单 (`themes.json`) 以及社区和官方主题的源代码。

## 📦 安装方法

### 方法 1：应用内市场（推荐）
1. 打开 **RelayCraft**。
2. 进入 **设置 (Settings)** -> **外观 (Appearance)**。
3. 点击 **浏览市场 (Browse Market)**。
4. 找到你喜欢的主题，点击 **安装 (Install)**。

### 方法 2：手动安装 (.rctheme)
1. 从 [Releases](https://github.com/relaycraft/relaycraft-themes/releases) 或其他来源下载主题包（例如 `neon-dark.rctheme`）。
2. 在 **设置** -> **插件/主题**（或外观）中，点击 **从文件安装 (Install from File)**。
3. 选择 `.rctheme` 或 `.zip` 文件。

## 📂 仓库结构

- `themes.json`: RelayCraft 用来发现主题的核心注册文件。
- `themes/`: 每个主题的源目录。
  - `theme-name/theme.yaml`: 元数据和颜色定义。
  - `theme-name/styles.css`: （可选）高级 CSS 覆盖。
  - `theme-name/assets/`: （可选）本地资源，如字体或背景图片。

## 🤝 贡献指南

我们欢迎社区贡献！请阅读 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md) 了解如何创建并提交你自己的主题。

## 📜 许可证

除非在主题子目录中另有说明，本仓库中的内容均采用 MIT 许可证授权。
