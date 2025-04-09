<template>
  <div class="page_search search_index">
	<div class="warp">
	  <div class="container">
		<div class="row">
		  <div class="col-12">
			<div class="card_result_search">
			  <div class="title">搜索结果</div>

				<!-- 文章搜索结果 -->
			  <list_result_search
				:list="result_article"
				title="音乐资讯"
				source_table="article"
			  ></list_result_search>

				<!-- 论坛搜索结果 -->
			  <list_result_search
				:list="result_forum"
				title="音乐论坛"
				source_table="forum"
			  ></list_result_search>

						  <list_result_search
				v-if="$check_action('/regular_users/list', 'get')"
				:list="result_regular_users_user_name"
				title="普通用户用户姓名"
				source_table="regular_users"
			  ></list_result_search>
								  <list_result_search
				v-if="$check_action('/regular_users/list', 'get')"
				:list="result_regular_users_user_gender"
				title="普通用户用户性别"
				source_table="regular_users"
			  ></list_result_search>
									  <list_result_search
				v-if="$check_action('/music_classification/list', 'get')"
				:list="result_music_classification_music_genre"
				title="音乐分类音乐类型"
				source_table="music_classification"
			  ></list_result_search>
									  <list_result_search
				v-if="$check_action('/popular_songs/list', 'get')"
				:list="result_popular_songs_song_title"
				title="热门歌曲歌曲名称"
				source_table="popular_songs"
			  ></list_result_search>
								  <list_result_search
				v-if="$check_action('/popular_songs/list', 'get')"
				:list="result_popular_songs_music_genre"
				title="热门歌曲音乐类型"
				source_table="popular_songs"
			  ></list_result_search>
																																	  <list_result_search
				v-if="$check_action('/music_evaluation/list', 'get')"
				:list="result_music_evaluation_song_title"
				title="音乐评价歌曲名称"
				source_table="music_evaluation"
			  ></list_result_search>
																										  <list_result_search
				v-if="$check_action('/music_evaluation/list', 'get')"
				:list="result_music_evaluation_scoring_score"
				title="音乐评价打分分数"
				source_table="music_evaluation"
			  ></list_result_search>
												  <list_result_search
				v-if="$check_action('/music_information/list', 'get')"
				:list="result_music_information_song_title"
				title="音乐信息歌曲名称"
				source_table="music_information"
			  ></list_result_search>
								  <list_result_search
				v-if="$check_action('/music_information/list', 'get')"
				:list="result_music_information_singer_name"
				title="音乐信息歌手名称"
				source_table="music_information"
			  ></list_result_search>
																					  <list_result_search
				v-if="$check_action('/music_data/list', 'get')"
				:list="result_music_data_song_title"
				title="音乐数据歌曲名称"
				source_table="music_data"
			  ></list_result_search>
								  <list_result_search
				v-if="$check_action('/music_data/list', 'get')"
				:list="result_music_data_singer_name"
				title="音乐数据歌手名称"
				source_table="music_data"
			  ></list_result_search>
																		  <list_result_search
				v-if="$check_action('/song_information/list', 'get')"
				:list="result_song_information_song_title"
				title="歌曲信息歌曲名称"
				source_table="song_information"
			  ></list_result_search>
								  <list_result_search
				v-if="$check_action('/song_information/list', 'get')"
				:list="result_song_information_singer_name"
				title="歌曲信息歌手名称"
				source_table="song_information"
			  ></list_result_search>
															</div>
		  </div>
		</div>
	  </div>
	</div>
  </div>
</template>

<script>
import mixin from "../../mixins/page.js";
import list_result_search from "../../components/diy/list_result_search.vue";

export default {
  mixins: [mixin],
  data() {
	return {
	  "query": {
		word: "",
	  },
	  "result_article": [],
	  "result_forum": [],
						"result_regular_users_user_name":[],
								"result_regular_users_user_gender":[],
									"result_music_classification_music_genre":[],
									"result_popular_songs_song_title":[],
								"result_popular_songs_music_genre":[],
																																	"result_music_evaluation_song_title":[],
																										"result_music_evaluation_scoring_score":[],
												"result_music_information_song_title":[],
								"result_music_information_singer_name":[],
																					"result_music_data_song_title":[],
								"result_music_data_singer_name":[],
																		"result_song_information_song_title":[],
								"result_song_information_singer_name":[],
													};
  },
  methods: {
	/**
	 * 获取文章
	 */
	get_article() {
	  this.$get("~/api/article/get_list?like=0", { page: 1, size: 10, title: this.query.word }, (json) => {
		if (json.result) {
		  this.result_article = json.result.list;
		}
	  });
	},
	/**
	 * 获取音乐论坛
	 */
	get_forum() {
	  this.$get("~/api/forum/get_list?like=0", { page: 1, size: 10, title: this.query.word }, (json) => {
		if (json.result) {
		  this.result_forum = json.result.list;
		}
	  });
	},

				/**
	 * 获取user_name
	 */
	get_regular_users_user_name(){
		let url = "~/api/regular_users/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "user_name": this.query.word }, (json) => {
		  if (json.result) {
			var result_regular_users_user_name = json.result.list;
			result_regular_users_user_name.map(o => o.title = o['user_name'])
	  			this.result_regular_users_user_name = result_regular_users_user_name
		 	}
		});
	},
						/**
	 * 获取user_gender
	 */
	get_regular_users_user_gender(){
		let url = "~/api/regular_users/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "user_gender": this.query.word }, (json) => {
		  if (json.result) {
			var result_regular_users_user_gender = json.result.list;
			result_regular_users_user_gender.map(o => o.title = o['user_gender'])
	  			this.result_regular_users_user_gender = result_regular_users_user_gender
		 	}
		});
	},
							/**
	 * 获取music_genre
	 */
	get_music_classification_music_genre(){
		let url = "~/api/music_classification/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "music_genre": this.query.word }, (json) => {
		  if (json.result) {
			var result_music_classification_music_genre = json.result.list;
			result_music_classification_music_genre.map(o => o.title = o['music_genre'])
	  			this.result_music_classification_music_genre = result_music_classification_music_genre
		 	}
		});
	},
							/**
	 * 获取song_title
	 */
	get_popular_songs_song_title(){
		let url = "~/api/popular_songs/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "song_title": this.query.word }, (json) => {
		  if (json.result) {
			var result_popular_songs_song_title = json.result.list;
			result_popular_songs_song_title.map(o => o.title = o['song_title'])
	  			this.result_popular_songs_song_title = result_popular_songs_song_title
		 	}
		});
	},
						/**
	 * 获取music_genre
	 */
	get_popular_songs_music_genre(){
		let url = "~/api/popular_songs/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "music_genre": this.query.word }, (json) => {
		  if (json.result) {
			var result_popular_songs_music_genre = json.result.list;
			result_popular_songs_music_genre.map(o => o.title = o['music_genre'])
	  			this.result_popular_songs_music_genre = result_popular_songs_music_genre
		 	}
		});
	},
																															/**
	 * 获取song_title
	 */
	get_music_evaluation_song_title(){
		let url = "~/api/music_evaluation/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "song_title": this.query.word }, (json) => {
		  if (json.result) {
			var result_music_evaluation_song_title = json.result.list;
			result_music_evaluation_song_title.map(o => o.title = o['song_title'])
	  			this.result_music_evaluation_song_title = result_music_evaluation_song_title
		 	}
		});
	},
																								/**
	 * 获取scoring_score
	 */
	get_music_evaluation_scoring_score(){
		let url = "~/api/music_evaluation/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "scoring_score": this.query.word }, (json) => {
		  if (json.result) {
			var result_music_evaluation_scoring_score = json.result.list;
			result_music_evaluation_scoring_score.map(o => o.title = o['scoring_score'])
	  			this.result_music_evaluation_scoring_score = result_music_evaluation_scoring_score
		 	}
		});
	},
										/**
	 * 获取song_title
	 */
	get_music_information_song_title(){
		let url = "~/api/music_information/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "song_title": this.query.word }, (json) => {
		  if (json.result) {
			var result_music_information_song_title = json.result.list;
			result_music_information_song_title.map(o => o.title = o['song_title'])
	  			this.result_music_information_song_title = result_music_information_song_title
		 	}
		});
	},
						/**
	 * 获取singer_name
	 */
	get_music_information_singer_name(){
		let url = "~/api/music_information/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "singer_name": this.query.word }, (json) => {
		  if (json.result) {
			var result_music_information_singer_name = json.result.list;
			result_music_information_singer_name.map(o => o.title = o['singer_name'])
	  			this.result_music_information_singer_name = result_music_information_singer_name
		 	}
		});
	},
																			/**
	 * 获取song_title
	 */
	get_music_data_song_title(){
		let url = "~/api/music_data/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "song_title": this.query.word }, (json) => {
		  if (json.result) {
			var result_music_data_song_title = json.result.list;
			result_music_data_song_title.map(o => o.title = o['song_title'])
	  			this.result_music_data_song_title = result_music_data_song_title
		 	}
		});
	},
						/**
	 * 获取singer_name
	 */
	get_music_data_singer_name(){
		let url = "~/api/music_data/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "singer_name": this.query.word }, (json) => {
		  if (json.result) {
			var result_music_data_singer_name = json.result.list;
			result_music_data_singer_name.map(o => o.title = o['singer_name'])
	  			this.result_music_data_singer_name = result_music_data_singer_name
		 	}
		});
	},
																/**
	 * 获取song_title
	 */
	get_song_information_song_title(){
		let url = "~/api/song_information/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "song_title": this.query.word }, (json) => {
		  if (json.result) {
			var result_song_information_song_title = json.result.list;
			result_song_information_song_title.map(o => o.title = o['song_title'])
	  			this.result_song_information_song_title = result_song_information_song_title
		 	}
		});
	},
						/**
	 * 获取singer_name
	 */
	get_song_information_singer_name(){
		let url = "~/api/song_information/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "singer_name": this.query.word }, (json) => {
		  if (json.result) {
			var result_song_information_singer_name = json.result.list;
			result_song_information_singer_name.map(o => o.title = o['singer_name'])
	  			this.result_song_information_singer_name = result_song_information_singer_name
		 	}
		});
	},
												
  },
  components: { list_result_search },
	created(){
    this.query.word = this.$route.query.word || "";
  },
  mounted() {
	this.get_article();
	this.get_forum();
					this.get_regular_users_user_name();
							this.get_regular_users_user_gender();
								this.get_music_classification_music_genre();
								this.get_popular_songs_song_title();
							this.get_popular_songs_music_genre();
																																this.get_music_evaluation_song_title();
																									this.get_music_evaluation_scoring_score();
											this.get_music_information_song_title();
							this.get_music_information_singer_name();
																				this.get_music_data_song_title();
							this.get_music_data_singer_name();
																	this.get_song_information_song_title();
							this.get_song_information_singer_name();
												  },
  watch: {
	$route() {
	  $.push(this.query, this.$route.query);
	  this.get_article();
	  this.get_forum();
				  this.get_regular_users_user_name();
						  this.get_regular_users_user_gender();
							  this.get_music_classification_music_genre();
							  this.get_popular_songs_song_title();
						  this.get_popular_songs_music_genre();
																															  this.get_music_evaluation_song_title();
																								  this.get_music_evaluation_scoring_score();
										  this.get_music_information_song_title();
						  this.get_music_information_singer_name();
																			  this.get_music_data_song_title();
						  this.get_music_data_singer_name();
																  this.get_song_information_song_title();
						  this.get_song_information_singer_name();
													},
  },
};
</script>

<style scoped>
.card_search {
  text-align: center;
}
.card_result_search>.title {
  text-align: center;
  padding: 10px 0;
}
</style>
