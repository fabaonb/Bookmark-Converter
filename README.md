<details>
<summary>中文文档</summary>

<div align="center">
  
# ![Bookmark Converter](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=2E9EF7&center=true&vCenter=true&width=600&height=50&lines=Bookmark+Converter)

**强大的 Chrome 和 Firefox 书签格式转换工具**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub code size](https://img.shields.io/github/languages/code-size/fabaonb/Bookmark-Converter.svg)](https://github.com/fabaonb/Bookmark-Converter)
[![GitHub downloads](https://img.shields.io/github/downloads/fabaonb/Bookmark-Converter/total.svg)](https://github.com/fabaonb/Bookmark-Converter/releases)
![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=fabaonb.Bookmark-Converter)

</div>

---

## ✨ 功能

- 将 Chrome 书签 JSON 文件转换为 Netscape Bookmark HTML 格式
- 将 Firefox 书签 SQLite 数据库转换为 Netscape Bookmark HTML 格式
- 支持去除外壳文件夹模式（去除"收藏夹栏"、"menu"、"toolbar"等外层容器）
- 无需额外依赖
- 跨平台支持（Windows、macOS、Linux）

## ⚡ 为什么选择这个工具？

浏览器自带的书签导入/导出功能速度很慢，尤其是书签数量较多时，可能需要等待很长时间。本工具直接解析书签文件，**转换速度极快**，即使有成千上万个书签也能瞬间完成。

---

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `bookmark_converter.pyw` | 标准转换脚本，保留完整书签结构 |
| `bookmark_converter_flat.pyw` | 扁平转换脚本，去除浏览器外层容器文件夹 |
| `dist/bookmark_converter.exe` | 标准转换可执行文件 |
| `dist/bookmark_converter_flat.exe` | 扁平转换可执行文件 |

---

## 🚀 使用方法

### 方式一：拖放使用（推荐）

直接将书签文件拖放到 `exe` 文件上即可自动转换。

### 方式二：命令行使用

```bash
# 标准转换
bookmark_converter.exe <书签文件路径>

# 扁平转换
bookmark_converter_flat.exe <书签文件路径>
```

---

## 📥 支持的输入格式

| 格式 | 扩展名 | 来源 |
|------|--------|------|
| Chrome JSON | `.json` 或无扩展名 | Chrome/Edge 书签文件 |
| Firefox SQLite | `.sqlite` / `.db` | Firefox places.sqlite |
| HTML | `.html` / `.htm` | 直接复制 |

---

## 📤 输出文件

- 标准转换：`原文件名_converted.html`
- 扁平转换：`原文件名_flat.html`

---

## 🌐 Chrome 书签位置

- Windows: `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks`
- macOS: `~/Library/Application Support/Google/Chrome/Default/Bookmarks`
- Linux: `~/.config/google-chrome/Default/Bookmarks`

---

## 🦊 Firefox 书签位置

- Windows: `%APPDATA%\Mozilla\Firefox\Profiles\<profile>\places.sqlite`
- macOS: `~/Library/Application Support/Firefox/Profiles/<profile>/places.sqlite`
- Linux: `~/.mozilla/firefox/<profile>/places.sqlite`

---

## ⚙️ 依赖

- Python 3.x
- 无需额外依赖（仅使用标准库）

---

## 🔨 编译 EXE

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole bookmark_converter.pyw
pyinstaller --onefile --noconsole bookmark_converter_flat.pyw
```



---

## 📄 许可证

[MIT License](LICENSE)

---


<div align="center">

**由 [LegViol](https://github.com/fabaonb) 用 ❤️ 制作**

**⭐ 如果您喜欢这个项目，请给它一个星标！ ⭐**

</div>

</details>


<div align="center">
  
# ![Bookmark Converter](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=2E9EF7&center=true&vCenter=true&width=600&height=50&lines=Bookmark+Converter)

**A powerful bookmark format converter for Chrome and Firefox**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub code size](https://img.shields.io/github/languages/code-size/fabaonb/Bookmark-Converter.svg)](https://github.com/fabaonb/Bookmark-Converter)
[![GitHub downloads](https://img.shields.io/github/downloads/fabaonb/Bookmark-Converter/total.svg)](https://github.com/fabaonb/Bookmark-Converter/releases)
![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=fabaonb.Bookmark-Converter)

</div>


---

## ✨ Features

- Convert Chrome bookmark JSON files to Netscape Bookmark HTML format
- Convert Firefox bookmark SQLite database to Netscape Bookmark HTML format
- Support flat mode (remove outer container folders like "Bookmarks Bar", "menu", "toolbar", etc.)
- No external dependencies required
- Cross-platform support (Windows, macOS, Linux)

## ⚡ Why Choose This Tool?

Browser's built-in bookmark import/export is slow, especially with many bookmarks - you may wait for a long time. This tool directly parses bookmark files and **converts instantly**, even with thousands of bookmarks.

---

## 📁 Files

| File | Description |
|------|-------------|
| `bookmark_converter.pyw` | Standard converter, preserves complete bookmark structure |
| `bookmark_converter_flat.pyw` | Flat converter, removes browser container folders |
| `dist/bookmark_converter.exe` | Standard converter executable |
| `dist/bookmark_converter_flat.exe` | Flat converter executable |

---

## 🚀 Usage

### Method 1: Drag & Drop (Recommended)

Simply drag and drop bookmark files onto the `exe` file.

### Method 2: Command Line

```bash
# Standard conversion
bookmark_converter.exe <bookmark_file_path>

# Flat conversion
bookmark_converter_flat.exe <bookmark_file_path>
```

---

## 📥 Supported Input Formats

| Format | Extension | Source |
|--------|-----------|--------|
| Chrome JSON | `.json` or no extension | Chrome/Edge bookmark file |
| Firefox SQLite | `.sqlite` / `.db` | Firefox places.sqlite |
| HTML | `.html` / `.htm` | Direct copy |

---

## 📤 Output Files

- Standard conversion: `filename_converted.html`
- Flat conversion: `filename_flat.html`

---

## 🌐 Chrome Bookmark Location

- Windows: `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks`
- macOS: `~/Library/Application Support/Google/Chrome/Default/Bookmarks`
- Linux: `~/.config/google-chrome/Default/Bookmarks`

---

## 🦊 Firefox Bookmark Location

- Windows: `%APPDATA%\Mozilla\Firefox\Profiles\<profile>\places.sqlite`
- macOS: `~/Library/Application Support/Firefox/Profiles/<profile>/places.sqlite`
- Linux: `~/.mozilla/firefox/<profile>/places.sqlite`

---

## ⚙️ Requirements

- Python 3.x
- No additional dependencies (standard library only)

---

## 🔨 Build EXE

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole bookmark_converter.pyw
pyinstaller --onefile --noconsole bookmark_converter_flat.pyw
```

---

## 📄 License

[MIT License](LICENSE)

---


<div align="center">

**Made with ❤️ by [LegViol](https://github.com/fabaonb)**

**⭐ If you like this project, give it a star! ⭐**

</div>
