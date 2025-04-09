<template>
	<el-main class="bg edit_wrap comtable_e">
		<el-form ref="form" :model="form" status-icon label-width="120px" v-if="is_view()">
		<el-row class="row_ce"> 
							<el-col v-if="user_group === '管理员' || $check_field('get','song_title') || $check_field('add','song_title') || $check_field('set','song_title')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌曲名称" prop="song_title">
												<el-input id="song_title" v-model="form['song_title']" placeholder="请输入歌曲名称"
							  v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','song_title')) || (!form['music_evaluation_id'] && $check_field('add','song_title'))" :disabled="disabledObj['song_title_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','song_title')">{{form['song_title']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','music_genre') || $check_field('add','music_genre') || $check_field('set','music_genre')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="音乐类型" prop="music_genre">
												<el-input id="music_genre" v-model="form['music_genre']" placeholder="请输入音乐类型"
							  v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','music_genre')) || (!form['music_evaluation_id'] && $check_field('add','music_genre'))" :disabled="disabledObj['music_genre_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','music_genre')">{{form['music_genre']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','singer_name') || $check_field('add','singer_name') || $check_field('set','singer_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="歌手姓名" prop="singer_name">
												<el-input id="singer_name" v-model="form['singer_name']" placeholder="请输入歌手姓名"
							  v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','singer_name')) || (!form['music_evaluation_id'] && $check_field('add','singer_name'))" :disabled="disabledObj['singer_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','singer_name')">{{form['singer_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','release_time') || $check_field('add','release_time') || $check_field('set','release_time')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="发行时间" prop="release_time">
								<el-date-picker :disabled="disabledObj['release_time_isDisabled']" v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','release_time')) || (!form['music_evaluation_id'] && $check_field('add','release_time'))" id="release_time"
						v-model="form['release_time']" type="date" placeholder="选择日期">
					</el-date-picker>
					<div v-else-if="$check_field('get','release_time')">{{form['release_time']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','album_name') || $check_field('add','album_name') || $check_field('set','album_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="专辑名称" prop="album_name">
												<el-input id="album_name" v-model="form['album_name']" placeholder="请输入专辑名称"
							  v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','album_name')) || (!form['music_evaluation_id'] && $check_field('add','album_name'))" :disabled="disabledObj['album_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','album_name')">{{form['album_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','regular_users') || $check_field('add','regular_users') || $check_field('set','regular_users')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="普通用户" prop="regular_users">
																		<div v-if="user_group !== '管理员'">
							{{ get_user_session_regular_users(form['regular_users']) }}
							<!--<el-input id="business_name" v-model="form['regular_users']" placeholder="请输入普通用户"-->
							<!--v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','regular_users')) || (!form['music_evaluation_id'] && $check_field('add','regular_users'))" :disabled="disabledObj['regular_users_isDisabled']"></el-input>-->
							<!--<div v-else-if="$check_field('get','regular_users')">{{form['regular_users']}}</div>-->
							<el-select v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','regular_users')) || (!form['music_evaluation_id'] && $check_field('add','regular_users'))" id="regular_users" v-model="form['regular_users']" :disabled="disabledObj['regular_users_isDisabled']">
								<el-option v-for="o in list_user_regular_users" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
										   :value="o['user_id']">
								</el-option>
							</el-select>
							<el-select v-else-if="$check_field('get','regular_users')" id="regular_users" v-model="form['regular_users']" :disabled="true">
								<el-option v-for="o in list_user_regular_users" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
										   :value="o['user_id']">
								</el-option>
							</el-select>
						</div>
						<el-select v-else id="regular_users" v-model="form['regular_users']" :disabled="disabledObj['regular_users_isDisabled']">
							<el-option v-for="o in list_user_regular_users" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
									   :value="o['user_id']">
							</el-option>
						</el-select>
																</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','user_name') || $check_field('add','user_name') || $check_field('set','user_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="用户姓名" prop="user_name">
												<el-input id="user_name" v-model="form['user_name']" placeholder="请输入用户姓名"
							  v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','user_name')) || (!form['music_evaluation_id'] && $check_field('add','user_name'))" :disabled="disabledObj['user_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','user_name')">{{form['user_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','scoring_score') || $check_field('add','scoring_score') || $check_field('set','scoring_score')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="打分分数" prop="scoring_score">
												<el-input id="scoring_score" v-model="form['scoring_score']" placeholder="请输入打分分数"
							  v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','scoring_score')) || (!form['music_evaluation_id'] && $check_field('add','scoring_score'))" :disabled="disabledObj['scoring_score_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','scoring_score')">{{form['scoring_score']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','evaluation_content') || $check_field('add','evaluation_content') || $check_field('set','evaluation_content')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="评价内容" prop="evaluation_content">
								<el-input type="textarea" id="evaluation_content" v-model="form['evaluation_content']" placeholder="请输入评价内容"
						v-if="user_group === '管理员' || (form['music_evaluation_id'] && $check_field('set','evaluation_content')) || (!form['music_evaluation_id'] && $check_field('add','evaluation_content'))" :disabled="disabledObj['evaluation_content_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','evaluation_content')">{{form['evaluation_content']}}</div>
							</el-form-item>
			</el-col>
					
	
	
	
	
	
	
		</el-row>
			<el-col :xs="24" :sm="12" :lg="8" class="el_form_btn_warp">
				<el-form-item v-if="$check_action('/music_evaluation/view','set') || $check_action('/music_evaluation/view','add') || $check_option('/music_evaluation/table','examine')">
					<el-button type="primary" @click="submit()">提交</el-button>
					<el-button @click="cancel()">取消</el-button>
				</el-form-item>
				<el-form-item v-else>
					<el-button @click="cancel()">返回</el-button>
				</el-form-item>
			</el-col>

		</el-form>
	</el-main>
</template>

<script>
	import mixin from "@/mixins/page.js";

	export default {
		mixins: [mixin],
		data() {
			return {
				field: "music_evaluation_id",
				url_add: "~/api/music_evaluation/add?",
				url_set: "~/api/music_evaluation/set?",
				url_get_obj: "~/api/music_evaluation/get_obj?",
				url_upload: "~/api/music_evaluation/upload?",

				query: {
					"music_evaluation_id": 0,
				},

				form: {
								"song_title":  '', // 歌曲名称
										"music_genre":  '', // 音乐类型
										"singer_name":  '', // 歌手姓名
										"release_time":  '', // 发行时间
										"album_name":  '', // 专辑名称
										"regular_users": 0, // 普通用户
										"user_name":  '', // 用户姓名
										"scoring_score":  '', // 打分分数
										"evaluation_content":  '', // 评价内容
											"music_evaluation_id": 0, // ID
						
				},
				disabledObj:{
								"song_title_isDisabled": false,
										"music_genre_isDisabled": false,
										"singer_name_isDisabled": false,
										"release_time_isDisabled": false,
										"album_name_isDisabled": false,
										"regular_users_isDisabled": false,
										"user_name_isDisabled": false,
										"scoring_score_isDisabled": false,
										"evaluation_content_isDisabled": false,
										},

	
		
		
		
		
		
					// 用户列表
				list_user_regular_users: [],
						// 用户组
				group_user_regular_users: "",
				
		
		
	
			}
		},
		methods: {


	
	
			
	
			
	
			
	
			
	
			
	
				/**
			 * 获取普通用户用户列表
			 */
			async get_list_user_regular_users() {
                // if(this.user_group !== "管理员" && this.form["regular_users"] === 0) {
                //     this.form["regular_users"] = this.user.user_id;
                // }
                var json = await this.$get("~/api/user/get_list?user_group=普通用户");
                if(json.result && json.result.list){
                    this.list_user_regular_users = json.result.list;
                }
                else if(json.error){
                    console.error(json.error);
                }
			},
					/**
			 * 获取普通用户用户组
			 */
			async get_group_user_regular_users() {
							this.form["regular_users"] = this.user.user_id;
							var json = await this.$get("~/api/user_group/get_obj?name=普通用户");
				if(json.result && json.result.obj){
					this.group_user_regular_users = json.result.obj;
				}
				else if(json.error){
					console.error(json.error);
				}
			},
			get_user_session_regular_users(id){
				var _this = this;
				var user_id = {"user_id":id}
				var url = "~/api/"+_this.group_user_regular_users.source_table+"/get_obj?"
				this.$get(url, user_id, function(res) {
					if (res.result && res.result.obj) {
						var arr = []
						for (let key in res.result.obj) {
							arr.push(key)
						}
						var arrForm = []
									for (let key in _this.form) {
							arrForm.push(key)
						}
												_this.form["regular_users"] = id
									_this.disabledObj['regular_users' + '_isDisabled'] = true
						for (var i=0;i<arr.length;i++){
						  if (arr[i]!=='examine_state' && arr[i]!=='examine_reply') {
							for (var j = 0; j < arrForm.length; j++) {
							  if (arr[i] === arrForm[j]) {
								if (arr[i] !== "regular_users") {
			                      _this.form[arrForm[j]] = res.result.obj[arr[i]]
			                      _this.disabledObj[arrForm[j] + '_isDisabled'] = true
								  break;
								} else {
								  _this.disabledObj[arrForm[j] + '_isDisabled'] = true
								}
							  }
							}
						  }
						}
					}
				});
			},
					get_user_regular_users(id){
				var obj = this.list_user_regular_users.getObj({"user_id":id});
				var ret = "";
				if(obj){
					if(obj.nickname){
						ret = obj.nickname;}
					else{
						ret = obj.username;
					}
				}
				return ret;
			},
			
	
			
	
			
	
		
			/**
			 * 获取对象之前
			 * @param {Object} param
			 */
			get_obj_before(param) {
				var form = "";
									// 获取缓存数据附加
				form = $.db.get("form");
							$.push(this.form ,form);
										
				if(this.form && form){
					Object.keys(this.form).forEach(key => {
						Object.keys(form).forEach(dbKey => {
							// if(dbKey === "charging_standard"){
							// 	this.form['charging_rules'] = form[dbKey];
							// 	this.disabledObj['charging_rules_isDisabled'] = true;
							// };
							if(key === dbKey){
								this.disabledObj[key+'_isDisabled'] = true;
							}
						})
					})
				}
								        if (this.form["release_time"] && this.form["release_time"].indexOf("-")===-1){
          this.form["release_time"] = this.$toTime(parseInt(this.form["release_time"]),"yyyy-MM-dd")
        }
															$.db.del("form");

				return param;
			},

			/**
			 * 获取对象之后
			 * @param {Object} json
			 * @param {Object} func
			 */
			get_obj_after(json, func){
																		if(this.form["release_time"]=="0000-00-00"){
				  this.form["release_time"] = null;
				}
				if(parseInt(this.form["release_time"]) > 9999){
					this.form["release_time"] = this.$toTime(parseInt(this.form["release_time"]),"yyyy-MM-dd")
				}
																							

			},

			/**
			 * 提交前验证事件
			 * @param {Object} 请求参数
			 * @return {String} 验证成功返回null, 失败返回错误提示
			 */
			submit_check(param) {
																																			if (!param.release_time){
					return "发行时间不能为空";
				}
																																																										return null;
			},

			is_view(){
				var bl = this.user_group == "管理员";

				if(!bl){
					bl = this.$check_action('/music_evaluation/table','add');
					console.log(bl ? "你有表格添加权限视作有添加权限" : "你没有表格添加权限");
				}
				if(!bl){
					bl = this.$check_action('/music_evaluation/table','set');
					console.log(bl ? "你有表格添加权限视作有修改权限" : "你没有表格修改权限");
				}
				if(!bl){
					bl = this.$check_action('/music_evaluation/view','add');
					console.log(bl ? "你有视图添加权限视作有添加权限" : "你没有视图添加权限");
				}
				if(!bl){
					bl = this.$check_action('/music_evaluation/view','set');
					console.log(bl ? "你有视图修改权限视作有修改权限" : "你没有视图修改权限");
				}
				if(!bl){
					bl = this.$check_action('/music_evaluation/view','get');
					console.log(bl ? "你有视图查询权限视作有查询权限" : "你没有视图查询权限");
				}

				console.log(bl ? "具有当前页面的查看权，请注意这不代表你有字段的查看权" : "无权查看当前页，请注意即便有字段查询权限没有页面查询权限也不行");

				return bl;
			},
			/**
			 * 上传文件
			 * @param {Object} param
			 */
			uploadimg(param) {
				this.uploadFile(param.file, "avatar");
			},

		},
		created() {
															this.get_list_user_regular_users();
					this.get_group_user_regular_users();
											},
	}
</script>

<style>
	.avatar-uploader .el-upload {
		border: 1px dashed #d9d9d9;
		border-radius: 6px;
		cursor: pointer;
		position: relative;
		overflow: hidden;
	}

	.avatar-uploader .el-upload:hover {
		border-color: #409EFF;
	}

	.avatar-uploader-icon {
		font-size: 28px;
		color: #8c939d;
		width: 178px;
		height: 178px;
		line-height: 178px;
		text-align: center;
	}

	.avatar {
		width: 178px;
		height: 178px;
		display: block;
	}




</style>
