<template>
	<div class="diy_edit page_i_want_to_customize" id="i_want_to_customize_edit">
		<div class='warp'>
			<div class='container'>
				<div class='row diy_edit_content_box'>
						<div v-if="$check_field('set','trade_name') || $check_field('add','trade_name') || $check_field('get','trade_name')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								商品名称:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_trade_name" v-model="form['trade_name']" placeholder="请输入商品名称" v-if="(form['trade_name'] && $check_field('set','trade_name')) || (!form['trade_name'] && $check_field('add','trade_name'))"  :disabled="disabledObj['trade_name_isDisabled']"/>
							<span v-else-if="$check_field('get','trade_name')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','seller_account') || $check_field('add','seller_account') || $check_field('get','seller_account')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								卖家账号:
							</span>
						</div>
						<div class="diy_field diy_down">
							<select id="form_seller_account" :disabled="disabledObj['seller_account_isDisabled']" v-model="form['seller_account']" v-if="(form['seller_account'] && $check_field('set','seller_account')) || (!form['seller_account'] && $check_field('add','seller_account'))" >
								<option v-for="o in list_user_seller_account" :value="o['user_id']">
									{{o['nickname'] + '-' + o['username']}}
								</option>
							</select>
							<span v-else-if="$check_field('get','seller_account')">{{ form['seller_account'] }}</span>
						</div>
					</div>
							<div v-if="$check_field('set','purchase_quantity') || $check_field('add','purchase_quantity') || $check_field('get','purchase_quantity')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								购买数量:
							</span>
						</div>
								<!-- 数字 -->
						<div class="diy_field diy_number">
							<input type="number" id="form_purchase_quantity" v-model.number="form['purchase_quantity']" placeholder="请输入购买数量" v-if="(form['purchase_quantity'] && $check_field('set','purchase_quantity')) || (!form['purchase_quantity'] && $check_field('add','purchase_quantity'))" :disabled="disabledObj['purchase_quantity_isDisabled']" />
							<span v-else-if="$check_field('get','purchase_quantity')">{{ form['${obj.name}'] }}</span>
						</div>
							</div>
							<div v-if="$check_field('set','price') || $check_field('add','price') || $check_field('get','price')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								价格:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_price" v-model="form['price']" placeholder="请输入价格" v-if="(form['price'] && $check_field('set','price')) || (!form['price'] && $check_field('add','price'))"  :disabled="disabledObj['price_isDisabled']"/>
							<span v-else-if="$check_field('get','price')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','total_amount') || $check_field('add','total_amount') || $check_field('get','total_amount')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								总金额:
							</span>
						</div>
								<!-- 文本 -->
									<div class="diy_field diy_text">
							<input type="text" id="form_total_amount" v-model="form['total_amount']" placeholder="请输入总金额" v-if="(form['total_amount'] && $check_field('set','total_amount')) || (!form['total_amount'] && $check_field('add','total_amount'))"  @focus="set_total_amount()" :disabled="disabledObj['total_amount_isDisabled']"/>
							<span v-else-if="$check_field('get','total_amount')">{{ form['${obj.name}'] }}</span>
						</div>
										</div>
							<div v-if="$check_field('set','user_number') || $check_field('add','user_number') || $check_field('get','user_number')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								用户编号:
							</span>
						</div>
						<div class="diy_field diy_down">
							<select id="form_user_number" :disabled="disabledObj['user_number_isDisabled']" v-model="form['user_number']" v-if="(form['user_number'] && $check_field('set','user_number')) || (!form['user_number'] && $check_field('add','user_number'))" >
								<option v-for="o in list_user_user_number" :value="o['user_id']">
									{{o['nickname'] + '-' + o['username']}}
								</option>
							</select>
							<span v-else-if="$check_field('get','user_number')">{{ form['user_number'] }}</span>
						</div>
					</div>
							<div v-if="$check_field('set','customized_requirements') || $check_field('add','customized_requirements') || $check_field('get','customized_requirements')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								定制要求:
							</span>
						</div>
								<!-- 多文本 -->
						<div class="diy_field diy_desc">
							<textarea id="form_customized_requirements" v-model="form['customized_requirements']" v-if="(form['customized_requirements'] && $check_field('set','customized_requirements')) || (!form['customized_requirements'] && $check_field('add','customized_requirements'))" :disabled="disabledObj['customized_requirements_isDisabled']" />
							<span v-else-if="$check_field('get','customized_requirements')">{{ form['${obj.name}'] }}</span>
						</div>
							</div>
							<div v-if="$check_field('set','related_pictures') || $check_field('add','related_pictures') || $check_field('get','related_pictures')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								相关图片:
							</span>
						</div>
								<!-- 图片 -->
						<input type="file" :disabled="disabledObj['related_pictures_isDisabled']" style="display: none;" id="form_img_related_pictures" title="related_pictures" @change="change_file($event.target.files,'related_pictures')"/>
						<!-- 修改权限 -->
						<div class="diy_field diy_img" v-if="form['related_pictures'] && $check_field('set','related_pictures')">
							<label for="form_img_related_pictures">
								<img :src="$fullUrl(form['related_pictures'])" />
							</label>
						</div>
						<!-- 添加权限 -->
						<div class="diy_field diy_img" v-else-if="!form['related_pictures'] && $check_field('add','related_pictures')">
							<label for="form_img_related_pictures">
								<div class="btn_add_img">
									<span>+</span>
								</div>
							</label>
						</div>
						<!-- 查询权限 -->
						<div class="diy_field diy_img" v-else-if="$check_field('get','related_pictures')">
							<img :src="$fullUrl(form['related_pictures'])" />
						</div>
							</div>
							<div v-if="$check_field('set','completion_time') || $check_field('add','completion_time') || $check_field('get','completion_time')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								完成时间:
							</span>
						</div>
								<!-- 日长 -->
						<div class="diy_field diy_datetime">
							<input type="datetime-local" :disabled="disabledObj['completion_time_isDisabled']" id="form_completion_time" v-model="form['completion_time']" placeholder="请输入完成时间" v-if="(form['completion_time'] && $check_field('set','completion_time')) || (!form['completion_time'] && $check_field('add','completion_time'))" />
							<span v-else-if="$check_field('get','completion_time')">{{ form['${obj.name}'] }}</span>
						</div>
							</div>
							<div v-if="$check_field('set','relevant_attachments') || $check_field('add','relevant_attachments') || $check_field('get','relevant_attachments')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								相关附件:
							</span>
						</div>
								<!-- 文件 -->
						<input type="file" style="display: none;" id="form_file_relevant_attachments" title="relevant_attachments" @change="change_file($event.target.files,'relevant_attachments')"/>
						<!-- 修改权限 -->
						<div class="diy_field diy_img" v-if="form['relevant_attachments'] && $check_field('set','relevant_attachments')">
							<label for="form_file_relevant_attachments">
								<!--<span>{{form['relevant_attachments']}} </span>-->
								<a :href="$fullUrl(form['relevant_attachments'])" target="_blank" style="color: rgb(64, 158, 255);">点击下载</a>
							</label>
						</div>
						<!-- 添加权限 -->
						<div class="diy_field diy_img" v-else-if="!form['relevant_attachments'] && $check_field('add','relevant_attachments')">
							<label for="form_file_relevant_attachments">
								<div class="btn_add_img">
									<span>+</span>
								</div>
							</label>
						</div>
						<!-- 查询权限 -->
						<div class="diy_field diy_img" v-else-if="$check_field('get','relevant_attachments')">
							<span>{{form['relevant_attachments']}} </span>
						</div>
							</div>
							<div v-if="$check_field('set','customized_video') || $check_field('add','customized_video') || $check_field('get','customized_video')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								定制视频:
							</span>
						</div>
								<!-- 视频 -->
						<div class="diy_field diy_video">
							<input type="file" id="form_video_customized_video" title="customized_video" @change="change_file($event.target.files,'customized_video')" v-if="(form['customized_video'] && $check_field('set','customized_video')) || (!form['customized_video'] && $check_field('add','customized_video'))" />
							<router-link :to="'/media/video?url=' + form['${obj.name}']" v-else-if="$check_field('get','customized_video')">查看视频</router-link>
						</div>
							</div>
							<div v-if="$check_field('set','customize_audio') || $check_field('add','customize_audio') || $check_field('get','customize_audio')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								定制音频:
							</span>
						</div>
								<!-- 音频 -->
						<div class="diy_field diy_music">
							<input type="file" id="form_music_customize_audio" title="customize_audio" @change="change_file($event.target.files,'customize_audio')" v-if="(form['customize_audio'] && $check_field('set','customize_audio')) || (!form['customize_audio'] && $check_field('add','customize_audio'))" />
							<router-link :to="'/media/music?url=' + form['${obj.name}']" v-else-if="$check_field('get','customize_audio')">聆听音频</router-link>
						</div>
							</div>
							<div v-if="$check_field('set','required_date') || $check_field('add','required_date') || $check_field('get','required_date')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								要求日期:
							</span>
						</div>
								<!-- 日期 -->
						<div class="diy_field diy_date">
							<input type="date" :disabled="disabledObj['required_date_isDisabled']" id="form_required_date" v-model="form['required_date']" placeholder="请输入要求日期" v-if="(form['required_date'] && $check_field('set','required_date')) || (!form['required_date'] && $check_field('add','required_date'))" />
							<span v-else-if="$check_field('get','required_date')">{{ form['${obj.name}'] }}</span>
						</div>
							</div>
							<div v-if="$check_field('set','custom_category') || $check_field('add','custom_category') || $check_field('get','custom_category')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								定制类别:
							</span>
						</div>
								<!-- 选项 -->
						<div class="diy_field diy_down">
							<select id="form_custom_category" v-model="form['custom_category']" v-if="(form['custom_category'] && $check_field('set','custom_category')) || (!form['custom_category'] && $check_field('add','custom_category'))" >
								<option v-for="o in list_custom_category" :value="o['custom_category']">
									{{ o['custom_category'] }}
								</option>
							</select>
							<span v-else-if="$check_field('get','custom_category')">{{ form['custom_category'] }}</span>
						</div>
							</div>
							<div v-if="$check_field('set','customization_details') || $check_field('add','customization_details') || $check_field('get','customization_details')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								定制详情:
							</span>
						</div>
								<!-- 多文本 -->
						<div class="diy_field diy_desc">
							<textarea id="form_customization_details" v-model="form['customization_details']" v-if="(form['customization_details'] && $check_field('set','customization_details')) || (!form['customization_details'] && $check_field('add','customization_details'))"  :disabled="disabledObj['customization_details_isDisabled']"/>
							<view v-else-if="$check_field('get','customization_details')" v-html="form['${obj.name}']"></view>
						</div>
							</div>
							<div v-if="$check_field('set','picking_category') || $check_field('add','picking_category') || $check_field('get','picking_category')" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								取货类别:
							</span>
						</div>
								<!-- 选项 -->
						<div class="diy_field diy_down">
							<select id="form_picking_category" v-model="form['picking_category']" v-if="(form['picking_category'] && $check_field('set','picking_category')) || (!form['picking_category'] && $check_field('add','picking_category'))" >
								<option v-for="o in list_picking_category" :value="o">
									{{o}}
								</option>
							</select>
							<span v-else-if="$check_field('get','picking_category')">{{ form['picking_category'] }}</span>
						</div>
							</div>
	


					<div v-if="user_group === '管理员' || $check_examine()" class="form-item col-12 col-md-6">
						<div class="diy_title">
							<span>
								审核状态:
							</span>
						</div>
						<div class="diy_field diy_select" v-if="$check_action('/i_want_to_customize/edit','examine')">
							<!--<span> {{ form['examine_state'] }} </span>-->
							<select v-model="form['examine_state']">
								<option value="未审核">
									未审核
								</option>
								<option value="已通过">
									已通过
								</option>
								<option value="未通过">
									未通过
								</option>
							</select>
						</div>
						<div class="diy_field diy_text" v-else>
							<span>
								{{ form['examine_state'] }}
							</span>
						</div>
					</div>


					<!-- 座位 -->
					<div class="form-item selected_seat_box col-12 col-md-6">
						<div class="seat-wrapper">
						  <div class="illustration">
							<div class="illustration-img-wrapper unselected-seat"></div>
							<span class="illustration-text">可选</span>
							<div class="illustration-img-wrapper selected-seat"></div>
							<span class="illustration-text">已选</span>
							<div class="illustration-img-wrapper bought-seat"></div>
							<span class="illustration-text">不可选</span>
							<div class="btn-buy" @click="buySeat">选定座位</div>
						  </div>
						  <div class="inner-seat-wrapper" ref="innerSeatWrapper">
							<div v-for="row in seatRow" :key="row">
							  <!--这里的v-if很重要，如果没有则会导致报错，因为seatArray初始状态为空-->
							  <div
								v-for="col in seatCol"
								v-if="seatArray.length > 0"
								class="seat"
								:style="{ width: seatSize + 'px', height: seatSize + 'px' }"
							  >
								<div
								  class="inner-seat"
								  @click="handleChooseSeat(row - 1, col - 1)"
								  v-if="seatArray[row - 1][col - 1] !== -1"
								  :class="
									seatArray[row - 1][col - 1] === 2
									  ? 'bought-seat'
									  : seatArray[row - 1][col - 1] === 1
									  ? 'selected-seat'
									  : 'unselected-seat'
								  "
								></div>
							  </div>
							</div>
						  </div>
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
				url_get_obj: "~/api/i_want_to_customize/get_obj?",
				url_add: "~/api/i_want_to_customize/add?",
				url_set: "~/api/i_want_to_customize/set?",

				// 登录权限
				oauth: {
					"signIn": true,
					"user_group": []
				},

				// 查询条件
				query: {
						"trade_name": "",
							"seller_account": 0,
							"purchase_quantity": 0,
							"price": "",
							"total_amount": "",
							"user_number": 0,
							"customized_requirements": "",
							"related_pictures": "",
							"completion_time": "",
							"relevant_attachments": "",
							"customized_video": "",
							"customize_audio": "",
							"required_date": "",
							"custom_category": "",
							"customization_details": "",
							"picking_category": "",
						"i_want_to_customize_id": 0,
					"seat": "", // 座位
				},

				obj: {
						"trade_name":  '', // 商品名称
							"seller_account": 0, // 卖家账号
							"purchase_quantity":  0, // 购买数量
							"price":  '', // 价格
							"total_amount":  '', // 总金额
							"user_number": 0, // 用户编号
							"customized_requirements":  '', // 定制要求
							"related_pictures":  '', // 相关图片
							"completion_time": new Date().getTime(),
							"relevant_attachments":  '', // 相关附件
							"customized_video":  '', // 定制视频
							"customize_audio":  '', // 定制音频
							"required_date": new Date().getTime(),
							"custom_category":  '', // 定制类别
							"customization_details":  '', // 定制详情
							"picking_category":  '', // 取货类别
						"examine_state": "未审核",
					"i_want_to_customize_id": 0,
					"seat": "", // 座位
          			"user_id": this.$store.state.user.user_id,
				},

				// 表单字段
				form: {
						"trade_name":  '', // 商品名称
							"seller_account": 0, // 卖家账号
							"purchase_quantity":  0, // 购买数量
							"price":  '', // 价格
							"total_amount":  '', // 总金额
							"user_number": 0, // 用户编号
							"customized_requirements":  '', // 定制要求
							"related_pictures":  '', // 相关图片
							"completion_time": new Date().getTime(),
							"relevant_attachments":  '', // 相关附件
							"customized_video":  '', // 定制视频
							"customize_audio":  '', // 定制音频
							"required_date": new Date().getTime(),
							"custom_category":  '', // 定制类别
							"customization_details":  '', // 定制详情
							"picking_category":  '', // 取货类别
						"examine_state": "未审核",
					"i_want_to_customize_id": 0,
					"seat": "", // 座位
          			"user_id": this.$store.state.user.user_id,
				},
				disabledObj:{
						"trade_name_isDisabled": false,
							"seller_account_isDisabled": false,
									"price_isDisabled": false,
							"total_amount_isDisabled": false,
							"user_number_isDisabled": false,
							"customized_requirements_isDisabled": false,
							"related_pictures_isDisabled": false,
							"completion_time_isDisabled": false,
							"relevant_attachments_isDisabled": false,
							"customized_video_isDisabled": false,
							"customize_audio_isDisabled": false,
							"required_date_isDisabled": false,
							"custom_category_isDisabled": false,
							"customization_details_isDisabled": false,
							"picking_category_isDisabled": false,
					},

								// 用户列表
				list_user_seller_account: [],
													// 用户列表
				list_user_user_number: [],
																				// 定制类别选项列表
				list_custom_category: [""],
									// 取货类别选项列表
				list_picking_category: ['送货上门','快递'],
		
				// ID字段
				field: "i_want_to_customize_id",

				//影院座位的二维数组,-1为非座位，0为未购座位，1为已选座位(绿色),2为已购座位(红色)
				seatArray: [],
				//影院座位行数
				seatRow: 5,
				//影院座位列数
				seatCol: 8,
				//座位尺寸
				seatSize: "",
				seatArr: [],
				list_: [],
				seatList: "",
        limit_times: 0, // 限制次数
        limit_type:0,
        act_limit_times:0,
			}
		},
		methods: {
      /**
       * 提交前验证事件
       * @param {Object} 请求参数
       * @return {String} 验证成功返回null, 失败返回错误提示
       */
      submit_check(param) {
        if(this.act_limit_times>=this.limit_times){
          return "已超过提交次数";
        }
        return null;
      },

      check_limit(){
        /**
         * 提交前验证事件
         * @param {Object} 请求参数
         * @return {String} 验证成功返回null, 失败返回错误提示
         */
        let _this = this;
        if (_this.$store.state.user.user_group==='管理员'){
          _this.limit_times = 999;
        }else {
          _this.$get("~/api/customized_goods/get_obj?",
              {"trade_name":_this.form.trade_name}, function(res) {
            if (res.result && res.result.obj) {
              _this.limit_times=res.result.obj.limit_times;
              _this.limit_type=res.result.obj.limit_type;
              let user_id = _this.$store.state.user.user_id;
              let limit_url = "~/api/i_want_to_customize/count?trade_name="+_this.form.trade_name+"&user_id="+user_id;
              if (_this.limit_type === 1){
                let day = _this.$toTime(parseInt((new Date()).getTime()), "yyyy-MM-dd");
                let time = "&create_time_min="+day+" 00:00:00&create_time_max="+day+" 23:59:59"
                limit_url = limit_url +time;
              }
              _this.$get(limit_url ,{}, function(res) {
                _this.act_limit_times = res.result;
              });
            }
          });
        }
      },
			
						/**
			 * 获取卖家用户列表
			 */
			async get_list_user_seller_account() {
				// if(this.user_group !== "管理员" && this.form["seller_account"] === 0) {
				//     this.form["seller_account"] = this.user.user_id;
				// }
				var json = await this.$get("~/api/user/get_list?user_group=卖家");
				if(json.result && json.result.list){
					this.list_user_seller_account = json.result.list;
				}
				else if(json.error){
					console.error(json.error);
				}
			},
		
				
				
				
									set_total_amount(){
				this.form.total_amount = parseFloat(this.form.purchase_quantity) * parseFloat(this.form.price)
        let r = /^\+?[1-9][0-9]*$/; // 正整数
        if(!r.test(this.form.total_amount) ){
          this.form.total_amount = this.form.total_amount.toFixed(2);
        }
			},
											/**
			 * 获取商城用户用户列表
			 */
			async get_list_user_user_number() {
				// if(this.user_group !== "管理员" && this.form["user_number"] === 0) {
				//     this.form["user_number"] = this.user.user_id;
				// }
				var json = await this.$get("~/api/user/get_list?user_group=商城用户");
				if(json.result && json.result.list){
					this.list_user_user_number = json.result.list;
				}
				else if(json.error){
					console.error(json.error);
				}
			},
					async get_user_session_user_number(){
				var _this = this;
				var json = await this.$get("~/api/user_group/get_obj?name=商城用户");
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
								_this.form["user_number"] = user_id
								_this.disabledObj['user_number' + '_isDisabled'] = true
								for (var i=0;i<arr.length;i++){
                  if (arr[i]!=='examine_state' && arr[i]!=='examine_reply') {
                    for (var j = 0; j < arrForm.length; j++) {
                      if (arr[i] === arrForm[j]) {
                        if (arr[i] !== "user_number") {
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
			 * 获取定制类别列表
			 */
			async get_list_custom_category() {
				var json = await this.$get("~/api/classification_information/get_list?");
				if(json.result && json.result.list){
					this.list_custom_category = json.result.list;
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
				this.$post("~/api/i_want_to_customize/upload?", form, (res) => {
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
																	        if (JSON.stringify(this.form["completion_time"]).indexOf("-")===-1) {
          this.form["completion_time"] = this.$toTime(parseInt(this.form["completion_time"]), "yyyy-MM-ddThh:mm")
        }
										        if (JSON.stringify(this.form["required_date"]).indexOf("-")===-1) {
          this.form["required_date"] = this.$toTime(parseInt(this.form["required_date"]), "yyyy-MM-dd")
        }
							
        $.db.del("form");
				this.get_list();
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

			// 选座
			//选定且购买座位
			buySeat: function () {
			  //遍历seatArray，将值为1的座位变为2
			  let oldArray = this.seatArray.slice();
			  for (let i = 0; i < this.seatRow; i++) {
				for (let j = 0; j < this.seatCol; j++) {
				  if (oldArray[i][j] === 1) {
					oldArray[i][j] = 2;
				  }
				}
			  }
			  this.seatArray = oldArray;
			  let string = "";
			  for (let x = 0; x < oldArray.length; x++) {
				let array = oldArray[x];
				for (let j = 0; j < array.length; j++) {
				  if (oldArray[x][j] === 2) {
					if (string == "") {
					  string = "" + (x * 8 + j);
					} else {
					  string = string + "," + (x * 8 + j);
					}
				  }
				}
			  }
			  // 对比判断哪些是新增的座位
			  let seat = this.obj.seat;
			  let seatB = "";
			  if (string != "" && string != null) {
				let stringList = string.split(",");
				let seatList = this.seatList;
				if (seatList.length != 0) {
				  let seatListArr = seatList.split(",");
				  for (let v = 0; v < stringList.length; v++) {
					if (
					  seatListArr.indexOf(stringList[v]) == -1 &&
					  seat.indexOf(stringList[v]) == -1
					) {
					  if (seat == "" || seat == null) {
						seat = stringList[v] + "";
						seatB = seat;
					  } else {
						if (seat.indexOf(stringList[v]) == -1) {
						  seat = seat + "," + stringList[v];
						  if (seatB == "" || seatB == null) {
							seatB = stringList[v];
						  } else {
							seatB = seatB + "," + stringList[v];
						  }
						}
					  }
					}
				  }
				} else {
				  seat = string;
				}
			  }

			  if (this.form.seat == "") {
				this.form.seat = seat;
			  } else {
				if (seatB != "") {
				  this.form.seat = this.form.seat + "," + seatB;
				}
			  }
			  this.seatList = string;

			},
			//处理座位选择逻辑
			handleChooseSeat: function (row, col) {
			  let seatValue = this.seatArray[row][col];
			  let newArray = this.seatArray;
			  //如果是已购座位，直接返回
			  if (seatValue === 2) return;
			  //如果是已选座位点击后变未选
			  if (seatValue === 1) {
				newArray[row][col] = 0;
			  } else if (seatValue === 0) {
				newArray[row][col] = 1;
			  }
			  //必须整体更新二维数组，Vue无法检测到数组某一项更新,必须slice复制一个数组才行
			  this.seatArray = newArray.slice();
			},
			/**
			 * 获取所有坐座位信息
			 */
			async get_list() {
			  var json = await this.$get("~/api/i_want_to_customize/get_list"
			  			  );
			  if (json.result && json.result.list) {
				this.list_ = json.result.list;
			  } else if (json.error) {
				console.error(json.error);
			  }
			  console.log(json);
			  let list = json.result.list;
			  if (list != null && list.length != 0) {
				let seatArr = "";
				for (let j = 0; j < list.length; j++) {
				  let seat = list[j].seat;
				  if (seat != null && seat != "") {
					if (seatArr == "") {
					  seatArr = seat + "";
					} else {
					  seatArr = seatArr + "," + seat;
					}
				  }
				}
				this.seatList = seatArr;
			  }
			  this.initSeatArray(5, 8);
			},

			//初始座位数组
			initSeatArray: function () {
			  let seatList = this.seatList;
			  let seatArr = seatList.split(",");
			  if (seatList == "" || seatList == null) {
				seatArr = [];
			  }
			  this.seatArr = seatArr;

			  let seatArray = Array(this.seatRow)
				.fill(0)
				.map(() => Array(this.seatCol).fill(0));
			  this.seatArray = seatArray;
			  for (let j = 0; j < seatArr.length; j++) {
				let i = Math.floor(seatArr[j] / 8);
				let x = seatArr[j] % 8;
				seatArray[i][x] = 2;
			  }
			  this.seatSize = this.$refs.innerSeatWrapper
				? parseInt(
					parseInt(
					  window.getComputedStyle(this.$refs.innerSeatWrapper).width,
					  10
					) / this.seatCol,
					10
				  )
				: 0;
			},
		},
		created() {
									this.get_list_user_seller_account();
															this.get_user_session_user_number();
					this.get_list_user_user_number();
																										this.get_list_custom_category();
											},
    watch: {
      'form.trade_name': {
        handler: function() {
          this.check_limit();
        }
      }
    }
	}
</script>

<style>


	.seat-wrapper {
	  margin-top: 20px;
	  height: 370px;
	  width: 500px;
	  border: 1px dotted #c5c5c5;
	  /* margin: 0 auto; */
	  position: relative;
	  overflow: hidden;
	}

	.inner-seat-wrapper {
	  position: absolute;
	  bottom: 0;
	  width: 100%;
	  box-sizing: border-box;
	}
	.seat {
	  float: left;
	  display: flex;
	  justify-content: center;
	  align-items: center;
	}
	.inner-seat {
	  width: 80%;
	  height: 80%;
	  cursor: pointer;
	}


	.btn-wrapper {
	  margin: 20px auto;
	  width: 1000px;
	  height: 30px;
	  text-align: center;
	}
	.btn-buy {
	  height: 100%;
	  line-height: 35px;
	  font-size: 15px;
	  border-radius: 5px;
	  padding: 0 5px;
	  background-color: #ffa349;
	  color: #ffffff;
	  display: inline-block;
	  cursor: pointer;
	  margin: 5px;
	}

	.illustration {
	  position: absolute;
	  left: 10px;
	  top: 20px;
	  height: 35px;
	  width: 300px;
	}
	.illustration-img-wrapper {
	  width: 25px;
	  height: 25px;
	  position: relative;
	  top: 50%;
	  display: inline-block;
	  transform: translateY(-50%);
	  margin-left: 10px;
	}
	.illustration-text {
	  display: inline-block;
	  height: 100%;
	  line-height: 35px;
	  font-size: 14px;
	  position: relative;
	  top: -2px;
	}


	    .selected-seat {
		background: url("../../../public/img/selected2.png") center center no-repeat;
		background-size: 100% 100%;
		}

		.unselected-seat {
		background: url("../../../public/img/unselected2.png") center center no-repeat;
		background-size: 100% 100%;
		}

		.bought-seat {
		background: url("../../../public/img/bought2.png") center center no-repeat;
		background-size: 100% 100%;
		}

</style>
