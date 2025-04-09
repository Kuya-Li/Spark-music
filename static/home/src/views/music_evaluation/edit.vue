<template>
	<div class="diy_edit page_music_evaluation" id="music_evaluation_edit">
		<div class='warp'>
			<div class='container'>
				<div class='row diy_edit_content_box'>
						<div v-if="$check_field('set','song_title') || $check_field('add','song_title') || $check_field('get','song_title')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								歌曲名称:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_song_title" v-model="form['song_title']" placeholder="请输入歌曲名称" v-if="(form['song_title'] && $check_field('set','song_title')) || (!form['song_title'] && $check_field('add','song_title'))"  :disabled="disabledObj['song_title_isDisabled']"/>
							<span v-else-if="$check_field('get','song_title')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','music_genre') || $check_field('add','music_genre') || $check_field('get','music_genre')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								音乐类型:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_music_genre" v-model="form['music_genre']" placeholder="请输入音乐类型" v-if="(form['music_genre'] && $check_field('set','music_genre')) || (!form['music_genre'] && $check_field('add','music_genre'))"  :disabled="disabledObj['music_genre_isDisabled']"/>
							<span v-else-if="$check_field('get','music_genre')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','singer_name') || $check_field('add','singer_name') || $check_field('get','singer_name')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								歌手姓名:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_singer_name" v-model="form['singer_name']" placeholder="请输入歌手姓名" v-if="(form['singer_name'] && $check_field('set','singer_name')) || (!form['singer_name'] && $check_field('add','singer_name'))"  :disabled="disabledObj['singer_name_isDisabled']"/>
							<span v-else-if="$check_field('get','singer_name')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','release_time') || $check_field('add','release_time') || $check_field('get','release_time')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								发行时间:
							</span>
						</div>
								<!-- 日期 -->
						<div class="diy_field diy_date">
							<input type="date" :disabled="disabledObj['release_time_isDisabled']" id="form_release_time" v-model="form['release_time']" placeholder="请输入发行时间" v-if="(form['release_time'] && $check_field('set','release_time')) || (!form['release_time'] && $check_field('add','release_time'))" />
							<span v-else-if="$check_field('get','release_time')">{{ form['${obj.name}'] }}</span>
						</div>
							</div>
							<div v-if="$check_field('set','album_name') || $check_field('add','album_name') || $check_field('get','album_name')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								专辑名称:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_album_name" v-model="form['album_name']" placeholder="请输入专辑名称" v-if="(form['album_name'] && $check_field('set','album_name')) || (!form['album_name'] && $check_field('add','album_name'))"  :disabled="disabledObj['album_name_isDisabled']"/>
							<span v-else-if="$check_field('get','album_name')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','regular_users') || $check_field('add','regular_users') || $check_field('get','regular_users')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								普通用户:
							</span>
						</div>
						<div class="diy_field diy_down">
							<select id="form_regular_users" :disabled="disabledObj['regular_users_isDisabled']" v-model="form['regular_users']" v-if="(form['regular_users'] && $check_field('set','regular_users')) || (!form['regular_users'] && $check_field('add','regular_users'))" >
								<option v-for="o in list_user_regular_users" :value="o['user_id']">
									{{o['nickname'] + '-' + o['username']}}
								</option>
							</select>
							<span v-else-if="$check_field('get','regular_users')">{{ form['regular_users'] }}</span>
						</div>
					</div>
							<div v-if="$check_field('set','user_name') || $check_field('add','user_name') || $check_field('get','user_name')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								用户姓名:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_user_name" v-model="form['user_name']" placeholder="请输入用户姓名" v-if="(form['user_name'] && $check_field('set','user_name')) || (!form['user_name'] && $check_field('add','user_name'))"  :disabled="disabledObj['user_name_isDisabled']"/>
							<span v-else-if="$check_field('get','user_name')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','scoring_score') || $check_field('add','scoring_score') || $check_field('get','scoring_score')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								打分分数:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_scoring_score" v-model="form['scoring_score']" placeholder="请输入打分分数" v-if="(form['scoring_score'] && $check_field('set','scoring_score')) || (!form['scoring_score'] && $check_field('add','scoring_score'))"  :disabled="disabledObj['scoring_score_isDisabled']"/>
							<span v-else-if="$check_field('get','scoring_score')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','evaluation_content') || $check_field('add','evaluation_content') || $check_field('get','evaluation_content')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								评价内容:
							</span>
						</div>
								<!-- 多文本 -->
						<div class="diy_field diy_desc">
							<textarea id="form_evaluation_content" v-model="form['evaluation_content']" v-if="(form['evaluation_content'] && $check_field('set','evaluation_content')) || (!form['evaluation_content'] && $check_field('add','evaluation_content'))" :disabled="disabledObj['evaluation_content_isDisabled']" />
							<span v-else-if="$check_field('get','evaluation_content')">{{ form['${obj.name}'] }}</span>
						</div>
							</div>
	




				</div>
				<div class="diy_edit_submit_box row">
					<div class="col-12">
						<div class="btn_box">
							<button class="btn_submit" @click="submit()">提交</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import mixin from "@/mixins/page.js";
	export default {
		mixins: [mixin],
		components: {},
		data() {
			return {
				url_get_obj: "~/api/music_evaluation/get_obj?",
				url_add: "~/api/music_evaluation/add?",
				url_set: "~/api/music_evaluation/set?",

				// 登录权限
				oauth: {
					"signIn": true,
					"user_group": []
				},

				// 查询条件
				query: {
						"song_title": "",
							"music_genre": "",
							"singer_name": "",
							"release_time": "",
							"album_name": "",
							"regular_users": 0,
							"user_name": "",
							"scoring_score": "",
							"evaluation_content": "",
						"music_evaluation_id": 0,
				},

				obj: {
						"song_title":  '', // 歌曲名称
							"music_genre":  '', // 音乐类型
							"singer_name":  '', // 歌手姓名
							"release_time": new Date().getTime(),
							"album_name":  '', // 专辑名称
							"regular_users": 0, // 普通用户
							"user_name":  '', // 用户姓名
							"scoring_score":  '', // 打分分数
							"evaluation_content":  '', // 评价内容
						"music_evaluation_id": 0,
				},

				// 表单字段
				form: {
						"song_title":  '', // 歌曲名称
							"music_genre":  '', // 音乐类型
							"singer_name":  '', // 歌手姓名
							"release_time": new Date().getTime(),
							"album_name":  '', // 专辑名称
							"regular_users": 0, // 普通用户
							"user_name":  '', // 用户姓名
							"scoring_score":  '', // 打分分数
							"evaluation_content":  '', // 评价内容
						"music_evaluation_id": 0,
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
							
				// ID字段
				field: "music_evaluation_id",

			}
		},
		methods: {
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
					async get_user_session_regular_users(){
				var _this = this;
				var json = await this.$get("~/api/user_group/get_obj?name=普通用户");
				if(json.result && json.result.obj){
					var source_table = json.result.obj.source_table;
					var user_id = _this.$store.state.user.user_id;
					if (user_id){
						var url = "~/api/"+source_table+"/get_obj?"
						this.$get(url, {"user_id":_this.$store.state.user.user_id}, function(res) {
							if (res.result && res.result.obj) {
								var arr = []
								for (let key in res.result.obj) {
									arr.push(key)
								}
								var arrForm = []
								for (let key in _this.form) {
									arrForm.push(key)
								}
								_this.form["regular_users"] = user_id
								_this.disabledObj['regular_users' + '_isDisabled'] = true
								for (var i=0;i<arr.length;i++){
                  if (arr[i]!=='examine_state' && arr[i]!=='examine_reply') {
                    for (var j = 0; j < arrForm.length; j++) {
                      if (arr[i] === arrForm[j]) {
                        if (arr[i] !== "regular_users") {
                          _this.form[arrForm[j]] = res.result.obj[arr[i]]
                          _this.disabledObj[arrForm[j] + '_isDisabled'] = true
                          break;
                        }
                      }
                    }
                  }
								}
							}
						});
					}
				}
				else if(json.error){
					console.error(json.error);
				}
			},
	
				
				
				
	
			/**
			 * 修改文件
			 * @param { Object } files 上传文件对象
			 * @param { String } str 表单的属性名
			 */
			change_file(files, str) {
				var form = new FormData();
				form.append("file", files[0]);
				this.$post("~/api/music_evaluation/upload?", form, (res) => {
					if (res.result) {
						this.form[str] = res.result.url;
					} else if (res.error) {
						this.$toast(res.error.message);
					}
				});
			},

			/**
			 * 获取对象后获取缓存表单
			 * @param {Object} json
			 * @param {Object} func
			 */
			get_obj_before(param){
				var form = $.db.get("form");
				// if (form) {
        //   delete(form.examine_state)
        //   delete(form.examine_reply)
        //   this.obj = $.push(this.obj ,form);
				// 	this.form = $.push(this.form ,form);
				// }
				// var arr = []
				// for (let key in form) {
				// 	arr.push(key)
				// }
				// for (var i=0;i<arr.length;i++){
				// 	this.disabledObj[arr[i] + '_isDisabled'] = true
				// }
        if (form) {
          var arr = []
          for (let key in form) {
            arr.push(key)
          }
          var arrForm = []
          for (let key in this.form) {
            arrForm.push(key)
          }
          for (var i=0;i<arr.length;i++){
            if (arr[i]!=='examine_state' && arr[i]!=='examine_reply') {
              for (var j = 0; j < arrForm.length; j++) {
                if (arrForm[j] === arr[i]) {
                  this.form[arrForm[j]] = form[arr[i]]
                  this.obj[arrForm[j]] = form[arr[i]]
                  this.disabledObj[arrForm[j] + '_isDisabled'] = true
                  break;
                }
              }
            }
          }
        }
								        if (this.form["release_time"] && JSON.stringify(this.form["release_time"]).indexOf("-")===-1) {
          this.form["release_time"] = this.$toTime(parseInt(this.form["release_time"]), "yyyy-MM-dd")
        }
											
        $.db.del("form");
				return param;
			},

			/**
			 * 获取对象后获取缓存表单
			 * @param {Object} json
			 * @param {Object} func
			 */
			get_obj_after(json ,func){
				// var form = $.db.get("form");
				// var obj = Object.assign({} ,form ,this.obj);
				// if (obj) {
        //   delete(obj.examine_state)
        //   delete(obj.examine_reply)
				// 	this.obj = $.push(this.obj ,obj);
				// }
				// if (form) {
        //   delete(form.examine_state)
        //   delete(form.examine_reply)
				// 	this.form = $.push(this.form ,form);
				// }

				if(func){
					func(json);
				}
			},

		},
		created() {
																				this.get_user_session_regular_users();
					this.get_list_user_regular_users();
												},
	}
</script>

<style>




</style>
