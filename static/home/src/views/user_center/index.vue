<template>
	<div class="page_user my_home" id="user_address">
		<div class="warp">
			<div class="container">
				<div class="row justify-content-between">
					<div class="col-12 col-md-3">
						<div class="card_menu">
							<!-- 左侧边栏 -->
							<list_admin_menu_user></list_admin_menu_user>
						</div>
					</div>
					<div class="col-12 col-md-9">
						<div class="card_addres pl-2">
							<div class="warp">
								<div class="container-fluid">
									<el-row>
										<div>欢迎来到个人中心</div>
									</el-row>
									<el-row>
											<el-col v-if="user_group == '管理员' || $check_figure('/regular_users/table')" :span="8">
											<div class="card chart">
																												<pieChart v-if="list_regular_users.length" id="list_regular_users" :list="list_regular_users" :title="'普通用户统计'"></pieChart>
												<div v-if="!list_regular_users.length">普通用户没有符合条件的数据</div>
																				</div>
										</el-col>
													<el-col v-if="user_group == '管理员' || $check_figure('/popular_songs/table')" :span="8">
											<div class="card chart">
														<stackedHorizontalBarChart v-if="bar_obj_popular_songs.values.length > 0" id="bar_obj_popular_songs" :vm="bar_obj_popular_songs" :title="'热门歌曲统计'">
												</stackedHorizontalBarChart>
												<div v-if="!bar_obj_popular_songs.values.length">热门歌曲没有符合条件的数据</div>
													</div>
										</el-col>
												<el-col v-if="user_group == '管理员' || $check_figure('/music_evaluation/table')" :span="8">
											<div class="card chart">
														<newBarChart v-if="bar_obj_music_evaluation.values.length > 0" id="bar_obj_music_evaluation" :vm="bar_obj_music_evaluation" :title="'音乐评价统计'">
												</newBarChart>
												<div v-if="!bar_obj_music_evaluation.values.length">音乐评价没有符合条件的数据</div>
													</div>
										</el-col>
												<el-col v-if="user_group == '管理员' || $check_figure('/music_information/table')" :span="8">
											<div class="card chart">
																												<doughnutChart v-if="list_music_information.length" id="list_music_information" :list="list_music_information" :title="'音乐信息统计'"></doughnutChart>
												<div v-if="!list_music_information.length">音乐信息没有符合条件的数据</div>
																																																</div>
										</el-col>
												<el-col v-if="user_group == '管理员' || $check_figure('/music_data/table')" :span="8">
											<div class="card chart">
																																			<pieChart v-if="list_music_data.length" id="list_music_data" :list="list_music_data" :title="'音乐数据统计'"></pieChart>
												<div v-if="!list_music_data.length">音乐数据没有符合条件的数据</div>
																																		</div>
										</el-col>
												<el-col v-if="user_group == '管理员' || $check_figure('/song_information/table')" :span="8">
											<div class="card chart">
																																										<doughnutChart v-if="list_song_information.length" id="list_song_information" :list="list_song_information" :title="'歌曲信息统计'"></doughnutChart>
												<div v-if="!list_song_information.length">歌曲信息没有符合条件的数据</div>
																											</div>
										</el-col>
										</el-row>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import list_admin_menu_user from "@/components/diy/list_admin_menu_user.vue";
	import pieChart from "@/components/charts/pie_chart";
	import newBarChart from "@/components/charts/new_bar_chart";
	import doughnutChart from "@/components/charts/doughnut_chart";
	import stackedHorizontalBarChart from "@/components/charts/stacked_horizontal_bar_chart";
	export default {
		data() {
			return {
					list_regular_users: [],
								bar_obj_popular_songs: {
					names:[],
					xAxis: [],
					values:[]
				},
						bar_obj_music_evaluation: {
					names:[],
					xAxis: [],
					values:[]
				},
						list_music_information: [],
						list_music_data: [],
						list_song_information: [],
				};
		},
		mounted() {
		},
		methods: {
			async get_nickname(list,flag){
				if (flag) {
					for (let i=0;i<list.length;i++){
						await this.$get(
								"~/api/user/get_obj?user_id="+list[i],
								null,
								(json) => {
									if (json.result) {
										list[i] = json.result.obj.nickname;
									}
								});
					}
				}else {
					for (let i=0;i<list.length;i++){
						await this.$get(
								"~/api/user/get_obj?user_id="+list[i].name,
								null,
								(json) => {
									if (json.result) {
										list[i].name = json.result.obj.nickname;
									}
								});
					}
				}
			},
														// 获取普通用户统计图数据
			get_list_regular_users() {
				let data = {};
								let flag = false;
												this.$get("~/api/regular_users/list_group?groupby=user_gender", data, (json) => {
					if (json.result) {
						var list = json.result.list;
						this.list_regular_users = list.map((o) => {
							return {
												name: o[1],
												value: o[0]
							};
						});
						if (flag){
							this.get_nickname(this.list_regular_users,false);
						}
					}
				});
			},
												// 获取热门歌曲统计图
			async get_list_popular_songs() {
				let name_list = [];
				let query_str = "";
									let group_by_value = "song_title";
								let flag = false;
												let date_flag = "其他"
																																																														name_list.push("播放数量");
				query_str = query_str+"playback_quantity"+","
																																	this.bar_obj_popular_songs.names = name_list
				query_str = query_str.substr(0,query_str.length-1);
				let data = {};
						await this.$get(
						"~/api/popular_songs/bar_group?field="+query_str+"&groupby="+group_by_value,
						data,
						(json) => {
							if (json.result) {
								let xAxis = [];
								let values = [];
								json.result.list.map((o) => {
									if (date_flag === "日期") {
										xAxis.push(this.$toTime(o[0] ,"yyyy-MM-dd"));
									}else if (date_flag === "时间") {
										xAxis.push(this.$toTime(o[0] ,"hh:mm:ss"));
									}else if (date_flag === "日长") {
										xAxis.push(this.$toTime(o[0] ,"yyyy-MM-dd hh:mm:ss"));
									}else {
										xAxis.push(o[0]);
									}
									values.push(o.splice(1))
								});
								this.bar_obj_popular_songs.xAxis = xAxis;
								this.bar_obj_popular_songs.values = values;
							}
							if (flag){
								this.get_nickname(this.bar_obj_popular_songs.xAxis,true);
							}
						});
			},
					// 获取音乐评价统计图
			async get_list_music_evaluation() {
				let name_list = [];
				let query_str = "";
									let group_by_value = "song_title";
								let flag = false;
												let date_flag = "其他"
																																																																						name_list.push("打分分数");
				query_str = query_str+"scoring_score"+","
																	this.bar_obj_music_evaluation.names = name_list
				query_str = query_str.substr(0,query_str.length-1);
				let data = {};
						let user_group = this.$store.state.user.user_group;
				let user_id = this.$store.state.user.user_id;
				if (user_group!='管理员'){
								let sqlwhere = "(";
																																																											if (user_group=="普通用户"){
						sqlwhere+= "regular_users = " + user_id + " or ";
					}
																																									if (sqlwhere.length>1){
						sqlwhere = sqlwhere.substr(0,sqlwhere.length-4);
						sqlwhere += ")";
						data.sqlwhere = sqlwhere;
					}
							}
						await this.$get(
						"~/api/music_evaluation/bar_group?field="+query_str+"&groupby="+group_by_value,
						data,
						(json) => {
							if (json.result) {
								let xAxis = [];
								let values = [];
								json.result.list.map((o) => {
									if (date_flag === "日期") {
										xAxis.push(this.$toTime(o[0] ,"yyyy-MM-dd"));
									}else if (date_flag === "时间") {
										xAxis.push(this.$toTime(o[0] ,"hh:mm:ss"));
									}else if (date_flag === "日长") {
										xAxis.push(this.$toTime(o[0] ,"yyyy-MM-dd hh:mm:ss"));
									}else {
										xAxis.push(o[0]);
									}
									values.push(o.splice(1))
								});
								this.bar_obj_music_evaluation.xAxis = xAxis;
								this.bar_obj_music_evaluation.values = values;
							}
							if (flag){
								this.get_nickname(this.bar_obj_music_evaluation.xAxis,true);
							}
						});
			},
															// 获取音乐信息统计图数据
			get_list_music_information() {
				let data = {};
								let flag = false;
												this.$get("~/api/music_information/list_group?groupby=singer_name", data, (json) => {
					if (json.result) {
						var list = json.result.list;
						this.list_music_information = list.map((o) => {
							return {
												name: o[1],
												value: o[0]
							};
						});
						if (flag){
							this.get_nickname(this.list_music_information,false);
						}
					}
				});
			},
																																													// 获取音乐数据统计图数据
			get_list_music_data() {
				let data = {};
								let flag = false;
												this.$get("~/api/music_data/list_group?groupby=album_name", data, (json) => {
					if (json.result) {
						var list = json.result.list;
						this.list_music_data = list.map((o) => {
							return {
												name: o[1],
												value: o[0]
							};
						});
						if (flag){
							this.get_nickname(this.list_music_data,false);
						}
					}
				});
			},
																																								// 获取歌曲信息统计图数据
			get_list_song_information() {
				let data = {};
								let flag = false;
												this.$get("~/api/song_information/list_group?groupby=release_time", data, (json) => {
					if (json.result) {
						var list = json.result.list;
						this.list_song_information = list.map((o) => {
							return {
												name: o[1],
												value: o[0]
							};
						});
						if (flag){
							this.get_nickname(this.list_song_information,false);
						}
					}
				});
			},
													},
		created() {
			setTimeout(() => {
				// 执行普通用户数据获取
			this.get_list_regular_users();
						// 执行热门歌曲数据获取
			this.get_list_popular_songs();
					// 执行音乐评价数据获取
			this.get_list_music_evaluation();
					// 执行音乐信息数据获取
			this.get_list_music_information();
					// 执行音乐数据数据获取
			this.get_list_music_data();
					// 执行歌曲信息数据获取
			this.get_list_song_information();
				}, 1000);
		},
		components: {
			pieChart,
			newBarChart,
			doughnutChart,
			stackedHorizontalBarChart,
			list_admin_menu_user
		},
	};
</script>

<style scoped>
	.container {
		min-height: 800px;
	}
</style>
