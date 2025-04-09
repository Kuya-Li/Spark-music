<template>
	<el-main class="bg table_wrap comtabel_t">
		<el-form label-position="right" :model="query" class="form p_4" label-width="120">
			<el-row class="rows row1">



							<el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
					<el-form-item label="歌曲名称">
									<el-input v-model="query.song_title"></el-input>
								</el-form-item>
				</el-col>
									<el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
					<el-form-item label="音乐类型">
									<el-select v-model="query.music_genre">
											<el-option v-for="o in list_music_genre" :key="o.music_genre" :label="o.music_genre"
								:value="o.music_genre">
							</el-option>
										</el-select>
								</el-form-item>
				</el-col>
																												</el-row>
	<el-row class="rows row2">

		<el-col :xs="24" :sm="24" :lg="24" class="search_btn_wrap search_btns">

				<el-col :xs="24" :sm="10" :lg="8" class="search_btn_1 search_btn_wrap_1 btns">

										<el-button type="primary" @click="search()" class="search_btn_find">查询</el-button>
						<el-button @click="reset()" style="margin-right: 74px;" class="search_btn_reset">重置</el-button>
																		

						<el-button v-if="user_group == '管理员' || $check_action('/popular_songs/table','del') || $check_action('/popular_songs/view','del')" class="search_btn_del" type="danger" @click="delInfo()">删除</el-button>
								
				</el-col>
		</el-col>
	</el-row >

		</el-form>
		<el-table :data="list" @selection-change="selectionChange" @sort-change="$sortChange" style="width: 100%" id="dataTable">
			<el-table-column fixed type="selection" tooltip-effect="dark" width="55">
			</el-table-column>
				<el-table-column prop="song_title" @sort-change="$sortChange" label="歌曲名称"
				v-if="user_group == '管理员' || $check_field('get','song_title')" min-width="200">
					</el-table-column>
					<el-table-column prop="music_genre" @sort-change="$sortChange" label="音乐类型"
				v-if="user_group == '管理员' || $check_field('get','music_genre')" min-width="200">
					</el-table-column>
					<el-table-column prop="singer_name" @sort-change="$sortChange" label="歌手姓名"
				v-if="user_group == '管理员' || $check_field('get','singer_name')" min-width="200">
					</el-table-column>
					<el-table-column prop="release_time" @sort-change="$sortChange" label="发行时间"
				v-if="user_group == '管理员' || $check_field('get','release_time')" min-width="200">
		                <template slot-scope="scope">
                	{{ $toTime(scope.row["release_time"],"yyyy-MM-dd") }}
                </template>
					</el-table-column>
					<el-table-column prop="singer_photos" @sort-change="$sortChange" label="歌手照片"
				v-if="user_group == '管理员' || $check_field('get','singer_photos')" min-width="200">
						<template slot-scope="scope">
					<el-image style="width: 100px; height: 100px" :src="$fullUrl(scope.row['singer_photos'])"
						:preview-src-list="[$fullUrl(scope.row['singer_photos'])]">
						<div slot="error" class="image-slot">
							<img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
						</div>
					</el-image>
				</template>
					</el-table-column>
					<el-table-column prop="album_name" @sort-change="$sortChange" label="专辑名称"
				v-if="user_group == '管理员' || $check_field('get','album_name')" min-width="200">
					</el-table-column>
					<el-table-column prop="playback_quantity" @sort-change="$sortChange" label="播放数量"
				v-if="user_group == '管理员' || $check_field('get','playback_quantity')" min-width="200">
					</el-table-column>
					<el-table-column prop="music_audio" @sort-change="$sortChange" label="音乐音频"
				v-if="user_group == '管理员' || $check_field('get','music_audio')" min-width="200">
						<template slot-scope="scope">
					<a href="javascript:void(0)" @click="music_audioAudioPlay($fullUrl(scope.row['music_audio']))" >点此播放</a>
				</template>
					</el-table-column>
					<el-table-column prop="music_introduction" @sort-change="$sortChange" label="音乐简介"
				v-if="user_group == '管理员' || $check_field('get','music_introduction')" min-width="200">
					</el-table-column>
					<el-table-column prop="music_content" @sort-change="$sortChange" label="音乐内容"
				v-if="user_group == '管理员' || $check_field('get','music_content')" min-width="200">
					</el-table-column>
	



            <el-table-column sortable prop="create_time" label="创建时间" min-width="200">
                <template slot-scope="scope">
                	{{ $toTime(scope.row["create_time"],"yyyy-MM-dd hh:mm:ss") }}
                </template>
            </el-table-column>

			<el-table-column sortable prop="update_time" label="更新时间" min-width="200">
                <template slot-scope="scope">
                	{{ $toTime(scope.row["update_time"],"yyyy-MM-dd hh:mm:ss") }}
                </template>
			</el-table-column>







			<el-table-column fixed="right" label="操作" min-width="200" v-if="user_group == '管理员' || $check_action('/popular_songs/table','set') || $check_action('/popular_songs/view','set') || $check_action('/popular_songs/view','get') || $check_action('/评分/table','add') || $check_action('/评分/view','add')" >


				<template slot-scope="scope">
					<div class="view_a">
					<router-link class="e-button el-button--small is-plain el-button--success" style="margin: 5px !important;"
					v-if="user_group == '管理员' || $check_action('/popular_songs/table','set') || $check_action('/popular_songs/view','set') || $check_action('/popular_songs/view','get')"
						:to="'./view?' + field + '=' + scope.row[field]"
						 size="small">
						<span>详情</span>
					</router-link>
						<router-link v-if="user_group == '管理员' || $check_comment('/popular_songs/table')" class="e-button el-button--small is-plain el-button--primary"
								  :to="'../comment/table?size=10&page=1&source_table=popular_songs&source_field=' + field + '&source_id=' + scope.row[field]" size="small">
						<span>查看评论</span>
					</router-link>
					</div>
				</template>
			</el-table-column>

		</el-table>

		<!-- 分页器 -->
		<div class="mt text_center">
			<el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
				:current-page="query.page" :page-sizes="[7, 10, 30, 100]" :page-size="query.size"
				layout="total, sizes, prev, pager, next, jumper" :total="count">
			</el-pagination>
		</div>
		<!-- /分页器 -->

											<el-dialog
					title="音频详情"
					:visible.sync="music_audioAudioPlayerModalVisible"
					width="30%"
			>
				<audio id="music_audioAudioPlayer" :src="music_audioAudioUrl" autoplay="autoplay" width="100%" controls>
					您的浏览器不支持Audio标签。
				</audio>
				<span slot="footer" class="dialog-footer">
					<el-button @click="music_audioCancelAudioModalVisible">取 消</el-button>
					</span>
			</el-dialog>
			
		<div class="modal_wrap" v-if="showModal">
			<div class="modal_box">
				<!-- <div class="modal_box_close" @click="closeModal">X</div> -->
				<p class="modal_box_title">重要提醒</p>
				<p class="modal_box_text">当前有数据达到预警值！</p>
				<div class="btn_box">
					<span @click="closeModal">取消</span>
					<span @click="closeModal">确定</span>
				</div>
			</div>
		</div>


	</el-main>
</template>
<script>
	import mixin from "@/mixins/page.js";

	export default {
		mixins: [mixin],
		data() {
			return {
				// 弹框
				showModal: false,
				// 获取数据地址
				url_get_list: "~/api/popular_songs/get_list?like=0",
				url_del: "~/api/popular_songs/del?",

				// 字段ID
				field: "popular_songs_id",

				// 查询
				query: {
					"size": 7,
					"page": 1,
								"song_title": "",
											"music_genre": "",
																"login_time": "",
					"create_time": "",
					"orderby": `create_time desc`
				},

				// 数据
				list: [],
												music_audioAudioPlayerModalVisible:false,
				music_audioAudioUrl:"",
										// 音乐类型列表
				list_music_genre: [""],
																					}
		},
		methods: {
			// 关闭弹框
			closeModal(){
				this.showModal = false;
				},


						/**
			 * 获取音乐类型列表
			 */
			async get_list_music_genre() {
				var json = await this.$get("~/api/music_classification/get_list?");
				if(json.result){
					this.list_music_genre = json.result.list;
				}else if (json.error){
					console.log(json.error);
				}
			},
																		



																			music_audioAudioPlay(v) {
				this.music_audioAudioUrl = v
				this.music_audioAudioPlayerModalVisible = true
			},

			music_audioCancelAudioModalVisible(){
				this.music_audioAudioUrl = ""
				this.music_audioAudioPlayerModalVisible = false
			},
							},
		created() {
						// 初始化音乐类型列表
			this.get_list_music_genre();
																				}
	}
</script>

<style type="text/css">
	.bg {
		background: white;
	}

	.form.p_4 {
		padding: 1rem;
	}

	.form .el-input {
		width: initial;
	}

	.mt {
		margin-top: 1rem;
	}

	.text_center {
		text-align: center;
	}

	.float-right {
		float: right;
	}


	.modal_wrap{
		width: 100vw;
		height: 100vh;
		position: fixed;
		top: 0;
		left: 0;
		background: rgba(0,0,0,0.5);
		z-index: 9999999999;
	}
	.modal_wrap .modal_box{
		width: 400px;
		height: 200px;
		background: url("../../assets/modal_bg.jpg") no-repeat center;
		background-size: cover;
		position: absolute;
		top: 50%;
		left: 50%;
		margin-left: -200px;
		margin-top: -100px;
		border-radius: 10px;
		}
	.modal_wrap .modal_box .modal_box_close{
		font-size: 20px;
		position: absolute;
		top: 10px;
		right: 10px;
		cursor: pointer;
		}
	.modal_wrap .modal_box .modal_box_title{
	  text-align: center;
    font-size: 18px;
    margin: 16px auto;
    color: #fff;
    border-bottom: 1px solid rgba(117, 116, 116,0.5);
    padding-bottom: 16px;
    width: 356px;
		}
	.modal_wrap .modal_box .modal_box_text{
			text-align: center;
		font-size: 15px;
		color: #fff;
		margin-top: 25px;
		}
	.modal_wrap .modal_box .btn_box{
		display: flex;
		flex-direction: row;
		justify-content: center;
		margin-top: 42px;
		}
			.modal_wrap .modal_box .btn_box span{
				display: inline-block;
				width: 80px;
				height: 30px;
				line-height: 30px;
				text-align: center;
				border: 1px solid #ccc;
				font-size: 14px;
				cursor: pointer;
				color: #fff;
			}
	.modal_wrap .modal_box .btn_box span:nth-child(2){
		background: #409EFF;
		color: #fff;
		border-color: #409EFF;
		margin-left: 15px;
	}
</style>
