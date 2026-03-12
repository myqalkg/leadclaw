# Lead-Claw (领爪) V1.2 设计蓝图 (Visual Specification)

## 1. 核心视觉规范 (Design System)
- **品牌色**: `#EA580C` (领爪橙 - 代表猎杀欲望和爆品热度)
- **辅助色**: `#111827` (灰黑 - 科技感/后端感), `#22C55E` (佣金绿 - 盈利可见)
- **字体**: 苹果/安卓系统原生黑体 (Inter + Noto Sans SC)

## 2. 核心页面设计 (Wireframe & Flow)

### A. [看板页] - Real-time Dashboard
- **Header**: 带有 "LIVE" 标记的神价监控心跳灯。
- **Stats Card**: 重点展示 [待分配佣金] —— 增强代理分发的动力。
- **Grid Layout**: 瀑布流展示，左上角评分气泡根据分值颜色渐变 (80+ 黄, 90+ 红)。

### B. [详情页] - Item Deep Dive
- **视觉图**: 大尺寸商详图。
- **AI 摘要**: "必买理由" —— 由 LLM 自动生成的短文本。
- **历史曲线**: 展示当前价格在近 30 天的位置（突出“神价”真实性）。

### C. [分发抽屉] - Distribution Drawer
- **转链反馈**: 侧滑出的抽屉，显示转链成功的 PID。
- **一键复制**: 自动生成文案 + 链接，适配微信对话框。

---

## 3. 设计原型 (代码预览 - 可直接访问)
我已经将最新的代码原型固封在:
`lead-claw/docs/preview/index.html`

## 4. 后续补充 (Assets)
- [ ] 微信小程序端适配页 (680px width)
- [ ] 钉钉/飞书消息推送卡片样式 (Adaptive Cards)
