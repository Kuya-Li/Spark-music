<template>
	<el-main class="bg edit_wrap">
		<el-form ref="form" :model="form" status-icon label-width="120px" v-if="is_view()">
		<el-row class="row_ce"> 
							<el-col v-if="user_group === '管理员' || $check_field('get','title') || $check_field('add','title') || $check_field('set','title')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="标题" prop="title">
												<el-input id="title" v-model="form['title']" placeholder="请输入标题"
							  v-if="user_group === '管理员' || (form['website_announcement_id'] && $check_field('set','title')) || (!form['website_announcement_id'] && $check_field('add','title'))" :disabled="disabledObj['title_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','title')">{{form['title']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','publisher') || $check_field('add','publisher') || $check_field('set','publisher')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="发布人" prop="publisher">
												<el-input id="publisher" v-model="form['publisher']" placeholder="请输入发布人"
							  v-if="user_group === '管理员' || (form['website_announcement_id'] && $check_field('set','publisher')) || (!form['website_announcement_id'] && $check_field('add','publisher'))" :disabled="disabledObj['publisher_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','publisher')">{{form['publisher']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','release_time') || $check_field('add','release_time') || $check_field('set','release_time')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="发布时间" prop="release_time">
								<el-date-picker :disabled="disabledObj['release_time_isDisabled']" v-if="user_group === '管理员' || (form['website_announcement_id'] && $check_field('set','release_time')) || (!form['website_announcement_id'] && $check_field('add','release_time'))" id="release_time"
						v-model="form['release_time']" type="datetime" placeholder="选择日期时间">
					</el-date-picker>
					<div v-else-if="$check_field('get','release_time')">{{form['release_time']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','relevant_accessories') || $check_field('add','relevant_accessories') || $check_field('set','relevant_accessories')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="相关附件" prop="relevant_accessories">
												<div v-if="disabledObj['relevant_accessories_isDisabled']">
						<div v-if="$check_field('get','relevant_accessories')">
							<el-button type="primary" @click="$download($fullUrl(form['relevant_accessories']),form['relevant_accessories'])">下载<i
									class="el-icon-download el-icon--right"></i></el-button>
						</div>
					</div>
					<div v-else>
						<el-upload v-if="user_group === '管理员' || (form['website_announcement_id'] && $check_field('set','relevant_accessories')) || (!form['website_announcement_id'] && $check_field('add','relevant_accessories'))" class="upload-demo" drag
								   action="" style="max-width: 300px;width: 100%;" :http-request="upload_relevant_accessories" :limit="1" accept="">
							<i class="el-icon-upload"></i>
							<div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
						</el-upload>
						<div v-else-if="$check_field('get','relevant_accessories')">
							<el-button type="primary" @click="$download($fullUrl(form['relevant_accessories']),form['relevant_accessories'])">下载<i
									class="el-icon-download el-icon--right"></i></el-button>
						</div>
					</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','details') || $check_field('add','details') || $check_field('set','details')" :xs="24" :sm="24" :lg="24" class="el_form_editor_warp">
				<el-form-item label="详情" prop="details">
					<quill-editor v-model.number="form['details']"
						v-if="user_group === '管理员' || (form['website_announcement_id'] && $check_field('set','details')) || (!form['website_announcement_id'] && $check_field('add','details')) ">
					</quill-editor>
					<div v-else-if="$check_field('get','details')" v-html="form['details']"></div>
				</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','lower_multi_test') || $check_field('add','lower_multi_test') || $check_field('set','lower_multi_test')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="下多测试" prop="lower_multi_test">
												<el-input id="lower_multi_test" v-model="form['lower_multi_test']" placeholder="请输入下多测试"
							  v-if="user_group === '管理员' || (form['website_announcement_id'] && $check_field('set','lower_multi_test')) || (!form['website_announcement_id'] && $check_field('add','lower_multi_test'))" :disabled="disabledObj['lower_multi_test_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','lower_multi_test')">{{form['lower_multi_test']}}</div>
											</el-form-item>
			</el-col>
					
	
	
	
	
	
	
	</el-row>
			<el-col :xs="24" :sm="12" :lg="8" class="el_form_btn_warp">
				<el-form-item>
					<el-button type="primary" @click="submit()">提交</el-button>
					<el-button @click="cancel()">取消</el-button>
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
				field: "website_announcement_id",
				url_add: "~/api/website_announcement/add?",
				url_set: "~/api/website_announcement/set?",
				url_get_obj: "~/api/website_announcement/get_obj?",
				url_upload: "~/api/website_announcement/upload?",

				query: {
					"website_announcement_id": 0,
				},

				form: {
								"title":  '', // 标题
										"publisher":  '', // 发布人
										"release_time":  '', // 发布时间
										"relevant_accessories":  '', // 相关附件
										"details":  '', // 详情
										"lower_multi_test":  '', // 下多测试
											"website_announcement_id": 0, // ID
						
				},
				disabledObj:{
								"title_isDisabled": false,
										"publisher_isDisabled": false,
										"release_time_isDisabled": false,
										"relevant_accessories_isDisabled": false,
										"details_isDisabled": false,
										"lower_multi_test_isDisabled": false,
										},

	
		
		
		
		
		
	
			}
		},
		methods: {


	
	
			
	
			
	
						/**
			 * 上传相关附件
			 * @param {Object} param 文件参数
			 */
			upload_relevant_accessories(param){
						this.uploadFile(param.file, "relevant_accessories");
					},
	
	
			
	
			
	
		
			/**
			 * 获取对象之前
			 * @param {Object} param
			 */
			get_obj_before(param) {
				var form = "";
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
					        if (this.form["release_time"].indexOf("-")===-1){
            this.form["release_time"] = this.$toTime(parseInt(this.form["release_time"]),"yyyy-MM-dd hh:mm:ss")
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


							        if(this.form["release_time"]=="0000-00-00 00:00:00"){
          this.form["release_time"] = null;
        }
				if(parseInt(this.form["release_time"]) > 9999){
					this.form["release_time"] = this.$toTime(parseInt(this.form["release_time"]),"yyyy-MM-dd hh:mm:ss")
				}
												


			},

			/**
			 * 提交前验证事件
			 * @param {Object} 请求参数
			 * @return {String} 验证成功返回null, 失败返回错误提示
			 */
			submit_check(param) {
				let msg = null
																								return msg;
			},

			is_view(){
				var bl = this.user_group == "管理员";

				if(!bl){
					bl = this.$check_action('/website_announcement/table','add');
					console.log(bl ? "你有表格添加权限视作有添加权限" : "你没有表格添加权限");
				}
				if(!bl){
					bl = this.$check_action('/website_announcement/table','set');
					console.log(bl ? "你有表格添加权限视作有修改权限" : "你没有表格修改权限");
				}
				if(!bl){
					bl = this.$check_action('/website_announcement/view','add');
					console.log(bl ? "你有视图添加权限视作有添加权限" : "你没有视图添加权限");
				}
				if(!bl){
					bl = this.$check_action('/website_announcement/view','set');
					console.log(bl ? "你有视图修改权限视作有修改权限" : "你没有视图修改权限");
				}
				if(!bl){
					bl = this.$check_action('/website_announcement/view','get');
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
