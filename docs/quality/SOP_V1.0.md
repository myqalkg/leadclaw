# Lead-Claw 标准化交付规范 (SOP v1.0)

## 🎨 A. 设计部 (Design Standard)
- **唯一合法底色**: `#f8f9fa` (禁止黑底/极客风格)。
- **核心组件必选**: `TabBar` (60px), `Safe-Area-Bottom`, `Auth-Float` (Black Gradient)。
- **字体规范**: 标题 `font-black`, 价格 `.voucher-price` (Red #ff0000)。

## 💻 B. 研发部 (Dev Protocol)
- **数据源**: 必须指向 `src/shared/burst_items.json`。
- **字段对齐**: `itemTitle`, `voucherPrice`, `originalPrice`, `score` (0-100)。
- **环境一致性**: 必须同时支持 Localhost 和 8000 端口公网映射。

## 📋 C. 质量部 (QA Check-list)
- [ ] 移动端首屏适配 (375px - 430px width)。
- [ ] 授权浮窗是否遮挡底部核心操作？
- [ ] 蜜源 API 响应状态码是否实时显示？

---
**执行准则**: 任何背离本规范的输出将被视为“脏提交”，必须立即回滚。
