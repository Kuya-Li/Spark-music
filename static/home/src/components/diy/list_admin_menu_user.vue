<template>
  <div class="list_menu diy_menu">
    <router-link
            to="/user_center/index"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/user_center/index'}"
     >
      <span class="left_span">个人首页</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
    <router-link
            to="/regular_users/table"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/regular_users/table'}"
            v-if="user_group == '管理员' || $check_action('/regular_users/table','get')">
      <span class="left_span">普通用户</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
    <router-link
            to="/music_classification/table"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/music_classification/table'}"
            v-if="user_group == '管理员' || $check_action('/music_classification/table','get')">
      <span class="left_span">音乐分类</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
    <router-link
            to="/popular_songs/table"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/popular_songs/table'}"
            v-if="user_group == '管理员' || $check_action('/popular_songs/table','get')">
      <span class="left_span">热门歌曲</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
    <router-link
            to="/music_evaluation/table"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/music_evaluation/table'}"
            v-if="user_group == '管理员' || $check_action('/music_evaluation/table','get')">
      <span class="left_span">音乐评价</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
    <router-link
            to="/music_information/table"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/music_information/table'}"
            v-if="user_group == '管理员' || $check_action('/music_information/table','get')">
      <span class="left_span">音乐信息</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
    <router-link
            to="/music_data/table"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/music_data/table'}"
            v-if="user_group == '管理员' || $check_action('/music_data/table','get')">
      <span class="left_span">音乐数据</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
    <router-link
            to="/song_information/table"
            class="menu_item"
            :class="{ selected: this.$route.path=== '/song_information/table'}"
            v-if="user_group == '管理员' || $check_action('/song_information/table','get')">
      <span class="left_span">歌曲信息</span>
      <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
    </router-link>
      <router-link
              to="/forum/table"
              class="menu_item"
              :class="{ selected: this.$route.path=== '/forum/table'}"
              v-if="user_group == '管理员' || $check_action('/forum/table','get')">
        <span class="left_span">{{$page_title("/forum/table") || "论坛"}}</span>
        <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
      </router-link>
      <router-link
              to="/message/table"
              class="menu_item"
              :class="{ selected: this.$route.path=== '/message/table'}"
              v-if="user_group == '管理员' || $check_action('/message/table','get')">
        <span class="left_span">留言板</span>
        <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
      </router-link>

  <router-link
              to="/user/collect"
              class="menu_item"
              :class="{ selected: this.$route.path=== '/collect/list'}"
              v-if="user_group == '管理员' || $check_action('/collect/list','get')">
        <span class="left_span">收藏</span>
        <span class="right_span"><b-icon icon="house-fill"></b-icon></span>
  </router-link>
  </div>
</template>

<script>
import mixin from "@/mixins/page.js";
export default {
  mixins: [mixin],
  data() {
    return {
    };
  },
  mounted() {
  },
  methods: {
  },

  components: {
  },
};
</script>

<style scoped>
.list_menu {
  flex: 0 0 25%;
  border-bottom: 1px solid #eee;
}
.menu_item {
  display: flex;
  justify-content: space-between;
  padding: 15px 20px;
  border: 1px solid #eee;
  border-bottom: none;
  background-color: #fff;
}
.menu_item.selected {
  background-color: #000;
}
.menu_item.selected span {
  color: #fff ;
}
.content {
  flex: 0 0 74%;
}
</style>
