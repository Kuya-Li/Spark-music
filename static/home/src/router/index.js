import Vue from 'vue';
import VueRouter from 'vue-router';
import index from '../views/index.vue'
import login from '../views/account/login.vue';

Vue.use(VueRouter)

const routes = [
	// 主页ss
	{
		path: '/',
		name: 'index',
		component: index
	},
	// 登录
	{
		path: '/account/login',
		name: 'login',
		component: login
	},
	// 忘记密码
	{
		path: '/account/forgot',
		name: 'forgot',
		component: () => import('../views/account/forgot.vue')
	},
	// 注册账号
	{
		path: '/account/register',
		name: 'register',
		component: () => import('../views/account/register.vue')
	},
	// 媒体图片
	{
		path: '/media/image',
		name: 'media_image',
		component: () => import('../views/media/image.vue')
	},
	// 音乐
	{
		path: '/media/music',
		name: 'media_music',
		component: () => import('../views/media/music.vue')
	},
	// 媒体视频
	{
		path: '/media/video',
		name: 'media_video',
		component: () => import('../views/media/video.vue')
	},
	// 媒体视频
	{
		path: '/user_center/index',
		name: 'user_center_index',
		component: () => import('../views/user_center/index.vue')
	},
	// 文章路由
	{
		path: '/article/list',
		name: 'article_list',
		component: () => import('../views/article/list.vue')
	},
	{
		path: '/article/details',
		name: 'article_details',
		component: () => import('../views/article/details.vue')
	},
	// 浏览网站
	// 收藏路由
	{
		path: '/user/collect',
		name: 'collect_list',
		component: () => import('../views/user/collect.vue')
	},

	// 论坛路由
	{
		path: '/forum/list',
		name: 'forum_list',
		component: () => import('../views/forum/list.vue')
	},

	{
		path: '/forum/details',
		name: 'forum_details',
		component: () => import('../views/forum/details.vue')
	},
	{
		path: '/forum/edit',
		name: 'forum_edit',
		component: () => import('../views/forum/edit.vue')
	},
	{
		path: '/forum/table',
		name: 'forum_table',
		component: () => import('../views/forum/table.vue')
	},
	{
		path: '/forum/view',
		name: 'forum_view',
		component: () => import('../views/forum/view.vue')
	},

	{
		path: '/comment/table',
		name: 'comment_table',
		component: () => import('../views/comment/table.vue')
	},
	{
		path: '/comment/view',
		name: 'comment_view',
		component: () => import('../views/comment/view.vue')
	},

	


	 // 留言路由
	 {
	 	path: '/message/list',
	 	name: 'message_list',
	 	component: () => import('../views/message/list.vue')
	 },
	 {
		path: '/message/edit',
		name: 'message_edit',
		component: () => import('../views/message/edit.vue')
	 },
	// 留言板路由
	{
		path: '/message/table',
		name: 'message_table',
		component: () => import('../views/message/table.vue')
	},
	{
		path: '/message/view',
		name: 'message_view',
		component: () => import('../views/message/view.vue')
	},

	// 公告路由
	{
		path: '/notice/list',
		name: 'notice_list',
		component: () => import('../views/notice/list.vue')
	},
	{
		path: '/notice/details',
		name: 'notice_details',
		component: () => import('../views/notice/details.vue')
	},
	// 普通用户表格路由
	{
		path: '/regular_users/table',
		name: '/regular_users_table',
		component: () => import('../views/regular_users/table.vue')
	},
	// 普通用户详情路由
	{
		path: '/regular_users/view',
		name: '/regular_users_view',
		component: () => import('../views/regular_users/view.vue')
	},
	
	
		// 音乐分类表格路由
	{
		path: '/music_classification/table',
		name: '/music_classification_table',
		component: () => import('../views/music_classification/table.vue')
	},
	// 音乐分类详情路由
	{
		path: '/music_classification/view',
		name: '/music_classification_view',
		component: () => import('../views/music_classification/view.vue')
	},
	
	
		// 热门歌曲表格路由
	{
		path: '/popular_songs/table',
		name: '/popular_songs_table',
		component: () => import('../views/popular_songs/table.vue')
	},
	// 热门歌曲详情路由
	{
		path: '/popular_songs/view',
		name: '/popular_songs_view',
		component: () => import('../views/popular_songs/view.vue')
	},
	
		// 热门歌曲列表路由
	{
		path: '/popular_songs/list',
		name: '/popular_songs_list',
		component: () => import('../views/popular_songs/list.vue')
	},
	
		// 热门歌曲详情路由
	{
		path: '/popular_songs/details',
		name: '/popular_songs_details',
		component: () => import('../views/popular_songs/details.vue')
	},
		// 音乐评价表格路由
	{
		path: '/music_evaluation/table',
		name: '/music_evaluation_table',
		component: () => import('../views/music_evaluation/table.vue')
	},
	// 音乐评价详情路由
	{
		path: '/music_evaluation/view',
		name: '/music_evaluation_view',
		component: () => import('../views/music_evaluation/view.vue')
	},
		// 音乐评价添加路由
	{
		path: '/music_evaluation/edit',
		name: '/music_evaluation_edit',
		component: () => import('../views/music_evaluation/edit.vue')
	},
	
	
		// 音乐信息表格路由
	{
		path: '/music_information/table',
		name: '/music_information_table',
		component: () => import('../views/music_information/table.vue')
	},
	// 音乐信息详情路由
	{
		path: '/music_information/view',
		name: '/music_information_view',
		component: () => import('../views/music_information/view.vue')
	},
	
		// 音乐信息列表路由
	{
		path: '/music_information/list',
		name: '/music_information_list',
		component: () => import('../views/music_information/list.vue')
	},
	
		// 音乐信息详情路由
	{
		path: '/music_information/details',
		name: '/music_information_details',
		component: () => import('../views/music_information/details.vue')
	},
		// 音乐数据表格路由
	{
		path: '/music_data/table',
		name: '/music_data_table',
		component: () => import('../views/music_data/table.vue')
	},
	// 音乐数据详情路由
	{
		path: '/music_data/view',
		name: '/music_data_view',
		component: () => import('../views/music_data/view.vue')
	},
	
		// 音乐数据列表路由
	{
		path: '/music_data/list',
		name: '/music_data_list',
		component: () => import('../views/music_data/list.vue')
	},
	
		// 音乐数据详情路由
	{
		path: '/music_data/details',
		name: '/music_data_details',
		component: () => import('../views/music_data/details.vue')
	},
		// 歌曲信息表格路由
	{
		path: '/song_information/table',
		name: '/song_information_table',
		component: () => import('../views/song_information/table.vue')
	},
	// 歌曲信息详情路由
	{
		path: '/song_information/view',
		name: '/song_information_view',
		component: () => import('../views/song_information/view.vue')
	},
	
		// 歌曲信息列表路由
	{
		path: '/song_information/list',
		name: '/song_information_list',
		component: () => import('../views/song_information/list.vue')
	},
	
		// 歌曲信息详情路由
	{
		path: '/song_information/details',
		name: '/song_information_details',
		component: () => import('../views/song_information/details.vue')
	},
	
	// 用户路由
	{
		path: '/user/index',
		name: 'user_index',
		component: () => import('../views/user/index.vue')
	},
	// 基本信息
	{
		path: '/user/info',
		name: 'user_info',
		component: () => import('../views/user/info.vue')
	},
	// 找回密码
	{
		path: '/user/password',
		name: 'user_password',
		component: () => import('../views/user/password.vue')
	},

	// 搜索
	{
		path: '/search',
		name: 'search',
		component: () => import('../views/search/index.vue')
	},
	// 局部搜索
	{
		path: '/search/details',
		name: 'search_details',
		component: () => import('../views/search/details.vue')
	}
]

const router = new VueRouter({
	mode: 'hash',
	base: process.env.BASE_URL,
	routes
})

router.afterEach((to, from, next) => {
	let title = "音乐推荐系统-home";
	document.title = title;
	document.logo = "音乐推荐系统"
})

export default router
