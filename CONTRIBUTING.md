# Contributing to RelayCraft Themes

[中文](CONTRIBUTING.zh-CN.md) | English

Thank you for your interest in creating a theme for RelayCraft! 🎨

## 🚀 Creating a Theme

A theme in RelayCraft is a simple folder structure that can be packaged into a `.rctheme` (zip) file.

### 1. Minimal Structure (Color-only)
For simple color customizations, you only need a `theme.yaml`.

**File Structure:**
```
my-theme/
└── theme.yaml
```

**theme.yaml:**
```yaml
id: "com.yourname.themes.my-theme"  # Unique ID (reverse domain style)
name: "My Cool Theme"
version: "1.0.0"
author: "Your Name"
type: "dark"  # or "light"
colors:
  # Base UI
  background: "#1e1e1e"
  foreground: "#d4d4d4"
  border: "#333333"
  
  # Brand
  primary: "#007acc"
  primary_foreground: "#ffffff"
  
  # Layout
  sidebar: "#252526"
  sidebar_foreground: "#f3f3f3"
  item_hover: "#2a2d2e"
  item_active: "#37373d"
```

### 2. Advanced Theme (CSS & Assets)
For full control, you can include custom CSS and local assets (fonts, images).

**File Structure:**
```
neon-dark/
├── theme.yaml
├── styles.css        # Custom CSS injection
└── assets/           # Local assets folder
    ├── background.png
    └── custom-font.woff2
```

**theme.yaml (Advanced):**
```yaml
id: "com.relaycraft.themes.neon-dark"
# ... metadata ...
css: "styles.css"  # Link your CSS file
```

**styles.css (Example):**
```css
/* Load a local font from assets/ */
@font-face {
  font-family: 'MyFont';
  src: url('assets/custom-font.woff2');
}

/* Apply to headers */
h1, h2, h3 {
  font-family: 'MyFont', sans-serif !important;
  text-shadow: 0 0 10px #00ffcc;
}

/* Use relative paths for images */
.sidebar {
  background-image: url('assets/background.png');
}
```

## 📦 Packaging Your Theme

1. Select all files inside your theme folder (`theme.yaml`, `styles.css`, `assets/`).
2. Zip them up.
3. Rename the `.zip` file extension to `.rctheme` (optional, but recommended).
   - e.g., `my-theme.rctheme`

## 📮 Submitting to the Registry

To make your theme available in the RelayCraft "Market", follow these steps:

1. **Fork** this repository.
2. Add your theme folder to the `themes/` directory (optional, but good for open source).
3. Host your `.rctheme` file somewhere accessible (e.g., GitHub Releases, or use the raw file link from this repo if you uploaded the source).
4. Edit `themes.json` to add your entry:

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

5. Submit a **Pull Request**.

## 🛠 Testing

Before submitting, verify your theme locally:
1. Open RelayCraft > Settings > Appearance.
2. Click "Install from File".
3. Select your `.rctheme` file.
4. Verify colors, fonts, and assets load correctly.
