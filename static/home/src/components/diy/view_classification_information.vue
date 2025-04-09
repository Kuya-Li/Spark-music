<template>
	<el-main class="bg edit_wrap">
		<el-form ref="form" :model="form" status-icon label-width="120px" v-if="is_view()">
		<el-row class="row_ce"> 
							<el-col v-if="user_group === '管理员' || $check_field('get','commodity_category') || $check_field('add','commodity_category') || $check_field('set','commodity_category')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="商品类别" prop="commodity_category">
												<el-input id="commodity_category" v-model="form['commodity_category']" placeholder="请输入商品类别"
							  v-if="user_group === '管理员' || (form['classification_information_id'] && $check_field('set','commodity_category')) || (!form['classification_information_id'] && $check_field('add','commodity_category'))" :disabled="disabledObj['commodity_category_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','commodity_category')">{{form['commodity_category']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','category') || $check_field('add','category') || $check_field('set','category')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="类别" prop="category">
												<el-input id="category" v-model="form['category']" placeholder="请输入类别"
							  v-if="user_group === '管理员' || (form['classification_information_id'] && $check_field('set','category')) || (!form['classification_information_id'] && $check_field('add','category'))" :disabled="disabledObj['category_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','category')">{{form['category']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','custom_category') || $check_field('add','custom_category') || $check_field('set','custom_category')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="定制类别" prop="custom_category">
												<el-input id="custom_category" v-model="form['custom_category']" placeholder="请输入定制类别"
							  v-if="user_group === '管理员' || (form['classification_information_id'] && $check_field('set','custom_category')) || (!form['classification_information_id'] && $check_field('add','custom_category'))" :disabled="disabledObj['custom_category_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','custom_category')">{{form['custom_category']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','categorize_multiple') || $check_field('add','categorize_multiple') || $check_field('set','categorize_multiple')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="分类下多" prop="categorize_multiple">
												<el-input id="categorize_multiple" v-model="form['categorize_multiple']" placeholder="请输入分类下多"
							  v-if="user_group === '管理员' || (form['classification_information_id'] && $check_field('set','categorize_multiple')) || (!form['classification_information_id'] && $check_field('add','categorize_multiple'))" :disabled="disabledObj['categorize_multiple_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','categorize_multiple')">{{form['categorize_multiple']}}</div>
											</el-form-item>
			</el-col>
					
	
	
				<el-col
					v-if="user_group === '管理员' || $check_action('/classification_information/view', 'set') || $check_action('/classification_information/view', 'add')"
					:xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="当前位置" prop="location_address">
					<el-input style="width: 80%" id="location_address" v-model="form['location_address']"
							  :disabled="true"></el-input>
					<el-button size="mini" @click="getLongitudeLatitude()">定位</el-button>
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
				field: "classification_information_id",
				url_add: "~/api/classification_information/add?",
				url_set: "~/api/classification_information/set?",
				url_get_obj: "~/api/classification_information/get_obj?",
				url_upload: "~/api/classification_information/upload?",

				query: {
					"classification_information_id": 0,
				},

				form: {
								"commodity_category":  '', // 商品类别
										"category":  '', // 类别
										"custom_category":  '', // 定制类别
										"categorize_multiple":  '', // 分类下多
											"classification_information_id": 0, // ID
							"location_address": "", // 定位地址
					"location_lng": "", // 定位地址经度
					"location_lat": "", // 定位地址纬度
					
				},
				disabledObj:{
								"commodity_category_isDisabled": false,
										"category_isDisabled": false,
										"custom_category_isDisabled": false,
										"categorize_multiple_isDisabled": false,
										},

	
		
		
		
	
			}
		},
		methods: {


	
	
			
	
			
	
			
	
		
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
												$.db.del("form");

				return param;
			},

			/**
			 * 获取对象之后
			 * @param {Object} json
			 * @param {Object} func
			 */
			get_obj_after(json, func){


												


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
					bl = this.$check_action('/classification_information/table','add');
					console.log(bl ? "你有表格添加权限视作有添加权限" : "你没有表格添加权限");
				}
				if(!bl){
					bl = this.$check_action('/classification_information/table','set');
					console.log(bl ? "你有表格添加权限视作有修改权限" : "你没有表格修改权限");
				}
				if(!bl){
					bl = this.$check_action('/classification_information/view','add');
					console.log(bl ? "你有视图添加权限视作有添加权限" : "你没有视图添加权限");
				}
				if(!bl){
					bl = this.$check_action('/classification_information/view','set');
					console.log(bl ? "你有视图修改权限视作有修改权限" : "你没有视图修改权限");
				}
				if(!bl){
					bl = this.$check_action('/classification_information/view','get');
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
			getLongitudeLatitude() {
				let _this = this;
				_this.form.location_address = "广东省深圳市南山区科技园";
				_this.form.location_lng = "113.946782";
				_this.form.location_lat = "22.556481";
				//如果该对象存在，那么地理位置服务可用。
				if ('geolocation' in navigator) {
					/* 地理位置服务可用 */
					let options = {
						enableHighAccuracy: true, //布尔值，表示系统是否使用最高精度来表示结果，注意，这会导致较慢的响应时间或者增加电量消耗（比如对于支持gps的移动设备来说）。如果值为false ，设备会通过更快响应以及/或者使用更少的电量等方法来尽可能的节约资源。默认值fasle
						timeout: 5000, //它表明的是设备必须在多长时间（单位毫秒）内返回一个位置。默认直到获取到位置才会返回值。
						maximumAge: 0 //表明可以返回多长时间（即最长年龄，单位毫秒）内的可获取的缓存位置。如果设置为 0, 说明设备不能使用一个缓存位置，而且必须去获取一个真实的当前位置。默认0
					}
					function success(position) {
						//position.coords (只读) 返回一个定义了当前位置的Coordinates对象。
						//position.timestamp (只读) 返回一个时间戳DOMTimeStamp， 这个时间戳表示获取到的位置的时间。
						let lat = position.coords.latitude //当前位置的纬度
						let lng = position.coords.longitude //当前位置精度
						let location=lng+","+lat;
						let url = "http://restapi.amap.com/v3/geocode/regeo?key=b6eb2819a6ba4c5119591614272fe7ca&location="+location;
						_this.$axios.get(url, {
						}).then((res) => {
							if (res.status===200){
								let data = res.data;
								if (data.status==='1'){
									_this.form.location_address = data.regeocode.formatted_address;
									_this.form.location_lng = JSON.stringify(lng);
									_this.form.location_lat = JSON.stringify(lat);
								}else {
									console.log(data.info)
								}
							}
						}).catch((res) => {
							console.log(res);
						});
					}
					function error(err) {
						let errorType = ['您拒绝共享位置信息', '获取不到位置信息', '获取位置信息超时']
						console.log(errorType[err.code - 1])
					}
					navigator.geolocation.getCurrentPosition(success, error, options)
				} else {
					/* 地理位置服务不可用 */
					console.log('无法获取您的位置，请检查定位是否开启或刷新重试')
				}
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
