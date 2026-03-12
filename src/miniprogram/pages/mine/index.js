Page({
  data: { userInfo: null, subscriptions: [] },
  onLoad: function() { this.fetchSubscriptions(); },
  handleLogin: function() {
    wx.getUserProfile({
      desc: '用于完善会员资料',
      success: (res) => {
        this.setData({ userInfo: res.userInfo });
        wx.showToast({ title: '登录成功', icon: 'success' });
        // 接下来这里会触发 wx.login 将 code 发给后端换 openid
      }
    })
  },
  fetchSubscriptions: function() {
    wx.request({
      url: 'https://opencloud-uat.gzmiyuan.com/my_subscriptions.json',
      success: (res) => { this.setData({ subscriptions: res.data }); }
    })
  }
})
