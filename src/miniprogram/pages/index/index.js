Page({
  data: { items: [] },
  onLoad: function() { this.fetchData(); },
  fetchData: function() {
    wx.request({
      url: 'https://opencloud-uat.gzmiyuan.com/burst_items.json',
      success: (res) => { if(res.data) this.setData({ items: res.data }); }
    })
  },
  
  handleGoBuy: function(e) {
    const item = e.currentTarget.dataset.item;
    wx.showLoading({ title: '正在为您安全转链...' });
    
    // 模拟服务端调用老板给的 /generateShare 接口
    // 真正的生产逻辑会将此请求发到我们自己的 backend，后端再安全调用蜜源
    setTimeout(() => {
      wx.hideLoading();
      const mock_kl = "1:/ f@o.dN 05/31 fu致..."; // 实际由接口返回
      wx.setClipboardData({
        data: mock_kl,
        success: () => {
          wx.showModal({
            title: '复制成功',
            content: '专属神价口令已复制，由于是体验版，请手动打开 App 领券购买',
            confirmText: '我知道了',
            showCancel: false
          });
        }
      });
    }, 1500);
  }
})
