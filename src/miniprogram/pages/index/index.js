Page({
  data: { items: [] },
  onLoad: function() { this.fetchData(); },
  fetchData: function() {
    wx.request({
      url: 'https://opencloud-uat.gzmiyuan.com/burst_items.json',
      success: (res) => { if(res.data) this.setData({ items: res.data }); }
    })
  },
  
  // 核心业务：跳转购买引擎
  handleGoBuy: function(e) {
    const item = e.currentTarget.dataset.item;
    wx.showActionSheet({
      itemList: ['立即领券购买', '分享给好友'],
      success: (res) => {
        if (res.tapIndex === 0) {
          // 跳转三方小程序逻辑 (示例跳转至淘宝/京东)
          wx.showModal({
            title: '引流确认',
            content: '由于负责人身份，正为您转向' + item.platform + '官方小程序领取专属神价券',
            success: (confirmRes) => {
              if (confirmRes.confirm) {
                // 真正的生产逻辑：wx.navigateToMiniProgram({ appId: '...', path: '...' })
                wx.showToast({ title: '由于未上线，暂模拟成功', icon: 'success' });
                console.log("跳转 Payload:", item);
              }
            }
          })
        }
      }
    })
  }
})
