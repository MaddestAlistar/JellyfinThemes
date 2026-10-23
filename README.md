# 良友 Jellyfin 主题库 · JellyfinThemes

[← 返回良友资源中心](https://maddestalistar.github.io/LiangYou-ResourceHub/) · 首版 2026-10-23

三个 **Jellyfin Web 自定义 CSS** 主题，直接复制文件全文即可试用；不包含外部字体或图片请求，方便本地/内网部署。

| 主题 | 特点 | 原始 CSS |
| --- | --- | --- |
| **黑金影院** | 暗金强调、影院氛围 | [black-gold.css](themes/black-gold.css) |
| **星云紫** | 蓝紫科技感 | [nebula-purple.css](themes/nebula-purple.css) |
| **极简石墨** | 低对比、克制的灰黑色系 | [minimal-graphite.css](themes/minimal-graphite.css) |

**[打开颜色与组件预览](preview/index.html)**（预览是静态设计模拟，并非真实 Jellyfin Web 截图）。

## 如何使用

1. 先备份 Jellyfin 管理后台中已有的自定义 CSS。
2. 浏览仓库 `themes/`，打开所选 CSS，复制全文。
3. 在 Jellyfin Web 的 **Dashboard → Branding → Custom CSS** 粘贴并保存；单用户可在 **Settings → Display** 使用自定义 CSS（具体路径因版本而异）。
4. 刷新 Jellyfin 网页并检查桌面与移动端，出现兼容问题时移除这段 CSS 即可恢复默认样式。

**兼容边界**：适用于 Jellyfin Web；第三方原生客户端未必支持；选择器、布局和控件在不同 Jellyfin Web 版本可能变化，尤其是 Jellyfin 12 等更新版本。暂未逐版本实机测试。无 JavaScript 与远程追踪内容，CSS 不修改媒体文件、数据库或后端设置。

官方参考：https://jellyfin.org/docs/general/clients/css-customization/ 

## 目录

`themes/` 可复制 CSS，`preview/index.html` 可本地打开对比主题风格，`scripts/validate.py` 检查主题文件完整性（非实机兼容测试）。
