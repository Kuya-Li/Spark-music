<template>
	<div class="diy_list page_popular_songs" id="popular_songs_list">
		<div class="warp">
			<div class="container diy_list_container">
				<div class="diy_list_title">
					<div class="col">
						<span class="title">热门歌曲列表</span>
					</div>
				</div>
				<div class="leis_box"> 
				<div class="iudis_box">
			
				<div class="row diy_list_search">
					<div class="col">
						<!-- 搜索栏 -->
						<div class="view Search">
							<span class="diy_list_search_title">关键字搜索：</span>
																							<b-form-input size="sm" class="mr-sm-2" placeholder="歌曲名称搜索" v-model="query['song_title']" />
																														<b-form-input size="sm" class="mr-sm-2" placeholder="音乐类型搜索" v-model="query['music_genre']" />
																																																																																																																																		<b-button size="sm" @click="search()" >
								<b-icon icon="search"/>
							</b-button>
						</div>
						<!-- /搜索栏 -->
					</div>
				</div>
				<div class="diy_list_select_box">
					<span class="diy_list_select_title">下拉搜索：</span>
						<div class="diy_list_dropdown_box">
						<div class="col">
							<!-- 筛选 -->
							<div class="view sift">
															<b-dropdown text="音乐类型" variant="outline-dark" left>
									<b-dropdown-item @click="filter_set('全部','music_genre')">全部</b-dropdown-item>
										<b-dropdown-item v-for="(o, i) in list_music_genre" :key="i" @click="filter_set(o['music_genre'],'music_genre')" >
												{{ o['music_genre'] }}
										</b-dropdown-item>
								</b-dropdown>
																			<!-- 排序 -->
							
								<b-dropdown text="排序" variant="outline-dark" left>
										<b-dropdown-item v-for="(o, i) in list_sort" :key="i" @click="set_sort(o)" >
												{{ o.name }}
										</b-dropdown-item>
								</b-dropdown>
						
							<!--/排序 -->
							</div>
							<!-- /筛选 -->
						</div>
					</div>
				
				</div>
			</div>
				<div class="row diy_list_box">
					<div class="col">
						<!-- 列表 -->
						<list_popular_songs :list="list" />
						<!-- /列表 -->
					</div>
				</div>
	</div>
	<!-- 大盒子结尾 -->
				<div class="row diy_list_page_box">
					<div class="col overflow-auto flex_cc">
						<!-- 分页器 -->
<!--						<diy_pager v-model="query['page']" :size="query['size']" :count="count" v-on:toPage="toPage" v-on:toSize="toSize" ></diy_pager>-->
            <b-pagination
                v-model="query.page"
                :total-rows="count"
                :per-page="query.size"
                @change="goToPage"
            />
						<!-- /分页器 -->
					</div>
				</div>
				<music_player :music-list="player_list"></music_player>
			</div>
		</div>
	</div>
</template>

<script>
	import list_popular_songs from "@/components/diy/list_popular_songs.vue";
	import diy_pager from "@/components/diy/diy_pager";
	import mixin from "@/mixins/page.js";
	import music_player from "@/components/diy/music_player.vue";

	export default {
		mixins: [mixin],
		components: {
			diy_pager,
			list_popular_songs,
			music_player,
		},
		data() {
			return {
				url_get_list: "~/api/popular_songs/get_list?like=0",

				// 查询条件
				query: {
					keyword: "",
					page: 1,
					size: 12,
								"song_title": "", // 歌曲名称
											"music_genre": "", // 音乐类型
															},
				player_list: [],
				// 排序内容
				list_sort: [{
						name: "创建时间从高到低",
						value: "create_time desc",
					},
					{
						name: "创建时间从低到高",
						value: "create_time asc",
					},
					{
						name: "更新时间从高到低",
						value: "update_time desc",
					},
					{
						name: "更新时间从低到高",
						value: "update_time asc",
					},
						{
						name: "歌曲名称正序",
						value: "song_title asc",
					},
					{
						name: "歌曲名称倒序",
						value: "song_title desc",
					},
							{
						name: "音乐类型正序",
						value: "music_genre asc",
					},
					{
						name: "音乐类型倒序",
						value: "music_genre desc",
					},
													],

							// 音乐类型列表
				"list_music_genre": [""],
																		
			}
		},
		methods: {
      get_list_before(param) {
      },
			/**
			 * 筛选选择
			 */
			filter_set(o,key) {
			    if (o == "全部") {
			        this.query[key] = "";
			    } else {
			        this.query[key] = o;
			    }
			    this.search();
			},

			/**
			 * 排序
			 */
			set_sort(o) {
			    this.query.orderby = o.value;
			    this.search();
			},
				/**
				 * 获取列表后
				 * @param {Object} json
				 * @param {Object} func
				 */
				get_list_after(json ,func){
					let list = json.result.list;
					for (let i = 0 ; i < list.length; i++){
						let obj = {};
									obj.music_name = list[i].song_title
																obj.singer = list[i].singer_name
																obj.cover = list[i].singer_photos
																					obj.audio_frequency = list[i].music_audio
																			this.player_list.push(obj)
					}
					if (func) {
						func(json);
					}
				},
					/**
			 * 获取音乐类型列表
			 */
			async get_list_music_genre() {
				var json = await this.$get("~/api/music_classification/get_list?");
				if (json.result) {
					this.list_music_genre = json.result.list;
				} else if (json.error) {
					console.log(json.error);
				}
			},
												/**
			 * 筛选
			 */
												filter_music_genre(o) {
				if (o == "全部") {
					this.query["music_genre"] = "";
				} else {
					this.query["music_genre"] = o;
				}
				this.search();
			},
																/**
			 * 重置
			 */
			reset() {
							this.query.song_title = ""
										this.query.music_genre = ""
															this.search();
			},

			// 返回条数
			toSize(i){
				this.query.size = i;
				this.first();
			},

			// 返回页数
			toPage(i){
				this.query.page = i;
				this.first();
			},

      goToPage(v){
        this.query.page = v;
        this.goToNew(v)
      },

		},
		computed: {
		},
		created() {
						/**
			 * 获取音乐类型列表
			 */
			this.get_list_music_genre();
																				}
	}
</script>

<style>
</style>
