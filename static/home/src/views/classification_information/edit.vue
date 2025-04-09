<template>
	<div class="diy_edit page_classification_information" id="classification_information_edit">
		<div class='warp'>
			<div class='container'>
				<div class='row diy_edit_content_box'>
						<div v-if="$check_field('set','commodity_category') || $check_field('add','commodity_category') || $check_field('get','commodity_category')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								商品类别:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_commodity_category" v-model="form['commodity_category']" placeholder="请输入商品类别" v-if="(form['commodity_category'] && $check_field('set','commodity_category')) || (!form['commodity_category'] && $check_field('add','commodity_category'))"  :disabled="disabledObj['commodity_category_isDisabled']"/>
							<span v-else-if="$check_field('get','commodity_category')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','category') || $check_field('add','category') || $check_field('get','category')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								类别:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_category" v-model="form['category']" placeholder="请输入类别" v-if="(form['category'] && $check_field('set','category')) || (!form['category'] && $check_field('add','category'))"  :disabled="disabledObj['category_isDisabled']"/>
							<span v-else-if="$check_field('get','category')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','custom_category') || $check_field('add','custom_category') || $check_field('get','custom_category')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								定制类别:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_custom_category" v-model="form['custom_category']" placeholder="请输入定制类别" v-if="(form['custom_category'] && $check_field('set','custom_category')) || (!form['custom_category'] && $check_field('add','custom_category'))"  :disabled="disabledObj['custom_category_isDisabled']"/>
							<span v-else-if="$check_field('get','custom_category')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','categorize_multiple') || $check_field('add','categorize_multiple') || $check_field('get','categorize_multiple')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								分类下多:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_categorize_multiple" v-model="form['categorize_multiple']" placeholder="请输入分类下多" v-if="(form['categorize_multiple'] && $check_field('set','categorize_multiple')) || (!form['categorize_multiple'] && $check_field('add','categorize_multiple'))"  :disabled="disabledObj['categorize_multiple_isDisabled']"/>
							<span v-else-if="$check_field('get','categorize_multiple')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
	




					<!-- 当前位置 -->
					<div class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>当前位置:
						</span>
						</div>
						<div class="diy_field diy_text">
							<input type="text" id="location_address" v-model="form['location_address']" :disabled="true"/>
						</div>
						<div class="diy_button">
							<button @click="getLongitudeLatitude()">定位</button>
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
				url_get_obj: "~/api/classification_information/get_obj?",
				url_add: "~/api/classification_information/add?",
				url_set: "~/api/classification_information/set?",

				// 登录权限
				oauth: {
					"signIn": true,
					"user_group": []
				},

				// 查询条件
				query: {
						"commodity_category": "",
							"category": "",
							"custom_category": "",
							"categorize_multiple": "",
						"classification_information_id": 0,
				},

				obj: {
						"commodity_category":  '', // 商品类别
							"category":  '', // 类别
							"custom_category":  '', // 定制类别
							"categorize_multiple":  '', // 分类下多
						"classification_information_id": 0,
					"location_address": "", // 定位地址
					"location_lng": "", // 定位地址经度
					"location_lat": "", // 定位地址纬度
				},

				// 表单字段
				form: {
						"commodity_category":  '', // 商品类别
							"category":  '', // 类别
							"custom_category":  '', // 定制类别
							"categorize_multiple":  '', // 分类下多
						"classification_information_id": 0,
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

								
				// ID字段
				field: "classification_information_id",

			}
		},
		methods: {
			
				
				
				
	
			/**
			 * 修改文件
			 * @param { Object } files 上传文件对象
			 * @param { String } str 表单的属性名
			 */
			change_file(files, str) {
				var form = new FormData();
				form.append("file", files[0]);
				this.$post("~/api/classification_information/upload?", form, (res) => {
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




</style>
