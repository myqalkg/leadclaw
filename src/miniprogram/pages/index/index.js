Page({
  data: { items: [] },
  onLoad: function() { this.fetchData(); },
  onImgError: function(e) { console.error("QA_IMG_ERROR:", e.detail.errMsg, "URL:", e.currentTarget.dataset.url); },
  onImgLoad: function(e) { console.log("QA_IMG_SUCCESS"); },
  fetchData: function() {
    wx.request({
      url: 'https://opencloud-uat.gzmiyuan.com/burst_items.json',
      success: (res) => { this.setData({ items: res.data }); }
    })
  }
})
