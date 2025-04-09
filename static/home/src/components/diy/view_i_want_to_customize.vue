<template>
	<el-main class="bg edit_wrap">
		<el-form ref="form" :model="form" status-icon label-width="120px" v-if="is_view()">
		<el-row class="row_ce"> 
							<el-col v-if="user_group === '管理员' || $check_field('get','trade_name') || $check_field('add','trade_name') || $check_field('set','trade_name')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="商品名称" prop="trade_name">
												<el-input id="trade_name" v-model="form['trade_name']" placeholder="请输入商品名称"
							  v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','trade_name')) || (!form['i_want_to_customize_id'] && $check_field('add','trade_name'))" :disabled="disabledObj['trade_name_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','trade_name')">{{form['trade_name']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','seller_account') || $check_field('add','seller_account') || $check_field('set','seller_account')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="卖家账号" prop="seller_account">
													<el-select v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','seller_account')) || (!form['i_want_to_customize_id'] && $check_field('add','seller_account'))" id="seller_account" v-model="form['seller_account']" :disabled="disabledObj['seller_account_isDisabled']">
							<el-option v-for="o in list_user_seller_account" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
									   :value="o['user_id']">
							</el-option>
						</el-select>
						<el-select v-else-if="$check_field('get','seller_account')" id="seller_account" v-model="form['seller_account']" :disabled="true">
							<el-option v-for="o in list_user_seller_account" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
									   :value="o['user_id']">
							</el-option>
						</el-select>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','purchase_quantity') || $check_field('add','purchase_quantity') || $check_field('set','purchase_quantity')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="购买数量" prop="purchase_quantity">
								<el-input-number id="purchase_quantity" v-model.number="form['purchase_quantity']"
						v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','purchase_quantity')) || (!form['i_want_to_customize_id'] && $check_field('add','purchase_quantity'))" :disabled="disabledObj['purchase_quantity_isDisabled']"></el-input-number>
					<div v-else-if="$check_field('get','purchase_quantity')">{{form['purchase_quantity']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','price') || $check_field('add','price') || $check_field('set','price')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="价格" prop="price">
												<el-input id="price" v-model="form['price']" placeholder="请输入价格"
							  v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','price')) || (!form['i_want_to_customize_id'] && $check_field('add','price'))" :disabled="disabledObj['price_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','price')">{{form['price']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','total_amount') || $check_field('add','total_amount') || $check_field('set','total_amount')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="总金额" prop="total_amount">
												<el-input id="total_amount" v-model="form['total_amount']" placeholder="请输入总金额"
							  v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','total_amount')) || (!form['i_want_to_customize_id'] && $check_field('add','total_amount'))"  @focus="set_total_amount()" :disabled="disabledObj['total_amount_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','total_amount')">{{form['total_amount']}}</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','user_number') || $check_field('add','user_number') || $check_field('set','user_number')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="用户编号" prop="user_number">
																		<div v-if="user_group !== '管理员'">
							{{ get_user_session_user_number(form['user_number']) }}
							<!--<el-input id="business_name" v-model="form['user_number']" placeholder="请输入用户编号"-->
							<!--v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','user_number')) || (!form['i_want_to_customize_id'] && $check_field('add','user_number'))" :disabled="disabledObj['user_number_isDisabled']"></el-input>-->
							<!--<div v-else-if="$check_field('get','user_number')">{{form['user_number']}}</div>-->
							<el-select v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','user_number')) || (!form['i_want_to_customize_id'] && $check_field('add','user_number'))" id="user_number" v-model="form['user_number']" :disabled="disabledObj['user_number_isDisabled']">
								<el-option v-for="o in list_user_user_number" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
										   :value="o['user_id']">
								</el-option>
							</el-select>
							<el-select v-else-if="$check_field('get','user_number')" id="user_number" v-model="form['user_number']" :disabled="true">
								<el-option v-for="o in list_user_user_number" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
										   :value="o['user_id']">
								</el-option>
							</el-select>
						</div>
						<el-select v-else id="user_number" v-model="form['user_number']" :disabled="disabledObj['user_number_isDisabled']">
							<el-option v-for="o in list_user_user_number" :key="o['username']" :label="o['nickname'] + '-' + o['username']"
									   :value="o['user_id']">
							</el-option>
						</el-select>
																</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','customized_requirements') || $check_field('add','customized_requirements') || $check_field('set','customized_requirements')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="定制要求" prop="customized_requirements">
								<el-input type="textarea" id="customized_requirements" v-model="form['customized_requirements']" placeholder="请输入定制要求"
						v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','customized_requirements')) || (!form['i_want_to_customize_id'] && $check_field('add','customized_requirements'))" :disabled="disabledObj['customized_requirements_isDisabled']"></el-input>
					<div v-else-if="$check_field('get','customized_requirements')">{{form['customized_requirements']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','related_pictures') || $check_field('add','related_pictures') || $check_field('set','related_pictures')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="相关图片" prop="related_pictures">
								<el-upload :disabled="disabledObj['related_pictures_isDisabled']" id="related_pictures" class="avatar-uploader" drag
						accept="image/gif, image/jpeg, image/png, image/jpg" action="" :http-request="upload_related_pictures"
						:show-file-list="false" v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','related_pictures')) || (!form['i_want_to_customize_id'] && $check_field('add','related_pictures'))">
						<img v-if="form['related_pictures']" :src="$fullUrl(form['related_pictures'])" class="avatar">
						<i v-else class="el-icon-plus avatar-uploader-icon"></i>
					</el-upload>
					<el-image v-else-if="$check_field('get','related_pictures')" style="width: 100px; height: 100px"
						:src="$fullUrl(form['related_pictures'])" :preview-src-list="[$fullUrl(form['related_pictures'])]">
						<div slot="error" class="image-slot">
							<img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
						</div>
					</el-image>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','completion_time') || $check_field('add','completion_time') || $check_field('set','completion_time')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="完成时间" prop="completion_time">
								<el-date-picker :disabled="disabledObj['completion_time_isDisabled']" v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','completion_time')) || (!form['i_want_to_customize_id'] && $check_field('add','completion_time'))" id="completion_time"
						v-model="form['completion_time']" type="datetime" placeholder="选择日期时间">
					</el-date-picker>
					<div v-else-if="$check_field('get','completion_time')">{{form['completion_time']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','relevant_attachments') || $check_field('add','relevant_attachments') || $check_field('set','relevant_attachments')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="相关附件" prop="relevant_attachments">
												<div v-if="disabledObj['relevant_attachments_isDisabled']">
						<div v-if="$check_field('get','relevant_attachments')">
							<el-button type="primary" @click="$download($fullUrl(form['relevant_attachments']),form['relevant_attachments'])">下载<i
									class="el-icon-download el-icon--right"></i></el-button>
						</div>
					</div>
					<div v-else>
						<el-upload v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','relevant_attachments')) || (!form['i_want_to_customize_id'] && $check_field('add','relevant_attachments'))" class="upload-demo" drag
								   action="" style="max-width: 300px;width: 100%;" :http-request="upload_relevant_attachments" :limit="1" accept="">
							<i class="el-icon-upload"></i>
							<div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
						</el-upload>
						<div v-else-if="$check_field('get','relevant_attachments')">
							<el-button type="primary" @click="$download($fullUrl(form['relevant_attachments']),form['relevant_attachments'])">下载<i
									class="el-icon-download el-icon--right"></i></el-button>
						</div>
					</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','customized_video') || $check_field('add','customized_video') || $check_field('set','customized_video')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="定制视频" prop="customized_video">
												<el-upload v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','customized_video')) || (!form['i_want_to_customize_id'] && $check_field('add','customized_video'))" class="upload-demo" drag
						action="" style="max-width: 300px;width: 100%;" :http-request="upload_customized_video" :limit="1" accept="video/ogg,video/mp4,video/webm">
						<i class="el-icon-upload"></i>
						<div class="el-upload__text">将视频拖到此处，或<em>点击上传</em></div>
					</el-upload>
					<div v-else-if="$check_field('get','customized_video')">
						<el-button type="primary" @click="download(form['customized_video'])">下载<i
								class="el-icon-download el-icon--right"></i></el-button>
					</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','customize_audio') || $check_field('add','customize_audio') || $check_field('set','customize_audio')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="定制音频" prop="customize_audio">
												<el-upload v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','customize_audio')) || (!form['i_want_to_customize_id'] && $check_field('add','customize_audio'))" class="upload-demo" drag
						action="" style="max-width: 300px;width: 100%;" :http-request="upload_customize_audio" :limit="1" accept="audio/ogg,audio/mp3,audio/wav">
						<i class="el-icon-upload"></i>
						<div class="el-upload__text">将音频拖到此处，或<em>点击上传</em></div>
					</el-upload>
					<div v-else-if="$check_field('get','customize_audio')">
						<el-button type="primary" @click="download(form['customize_audio'])">下载<i
								class="el-icon-download el-icon--right"></i></el-button>
					</div>
											</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','required_date') || $check_field('add','required_date') || $check_field('set','required_date')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="要求日期" prop="required_date">
								<el-date-picker :disabled="disabledObj['required_date_isDisabled']" v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','required_date')) || (!form['i_want_to_customize_id'] && $check_field('add','required_date'))" id="required_date"
						v-model="form['required_date']" type="date" placeholder="选择日期">
					</el-date-picker>
					<div v-else-if="$check_field('get','required_date')">{{form['required_date']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','custom_category') || $check_field('add','custom_category') || $check_field('set','custom_category')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="定制类别" prop="custom_category">
								<el-select id="custom_category" v-model="form['custom_category']"
						v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','custom_category')) || (!form['i_want_to_customize_id'] && $check_field('add','custom_category'))">
						<el-option v-for="o in list_custom_category" :key="o['custom_category']" :label="o['custom_category']"
							:value="o['custom_category']">
						</el-option>
					</el-select>
					<div v-else-if="$check_field('get','custom_category')">{{form['custom_category']}}</div>
							</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','customization_details') || $check_field('add','customization_details') || $check_field('set','customization_details')" :xs="24" :sm="24" :lg="24" class="el_form_editor_warp">
				<el-form-item label="定制详情" prop="customization_details">
					<quill-editor v-model.number="form['customization_details']"
						v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','customization_details')) || (!form['i_want_to_customize_id'] && $check_field('add','customization_details')) ">
					</quill-editor>
					<div v-else-if="$check_field('get','customization_details')" v-html="form['customization_details']"></div>
				</el-form-item>
			</el-col>
								<el-col v-if="user_group === '管理员' || $check_field('get','picking_category') || $check_field('add','picking_category') || $check_field('set','picking_category')" :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="取货类别" prop="picking_category">
								<el-select id="picking_category" v-model="form['picking_category']"
						v-if="user_group === '管理员' || (form['i_want_to_customize_id'] && $check_field('set','picking_category')) || (!form['i_want_to_customize_id'] && $check_field('add','picking_category'))">
						<el-option v-for="o in list_picking_category" :key="o" :label="o" :value="o">
						</el-option>
					</el-select>
					<div v-else-if="$check_field('get','picking_category')">{{form['picking_category']}}</div>
							</el-form-item>
			</el-col>
							<el-col :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
				<el-form-item label="审核状态" prop="examine_state">
					<el-select id="examine_state" v-model="form['examine_state']"
						v-if="user_group === '管理员' || (form['examine_state'] && $check_examine()) || (!form['examine_state'] && $check_examine())">
						<el-option key="未审核" label="未审核" value="未审核"></el-option>
						<el-option key="已通过" label="已通过" value="已通过"></el-option>
						<el-option key="未通过" label="未通过" value="未通过"></el-option>
					</el-select>
					<div v-else>{{form["examine_state"]}}</div>
				</el-form-item>
			</el-col>
		
	
	
	
				<el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
				<el-form-item label="选座" prop="seat">
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
					  <div v-for="row in seatRow">
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
				field: "i_want_to_customize_id",
				url_add: "~/api/i_want_to_customize/add?",
				url_set: "~/api/i_want_to_customize/set?",
				url_get_obj: "~/api/i_want_to_customize/get_obj?",
				url_upload: "~/api/i_want_to_customize/upload?",

				query: {
					"i_want_to_customize_id": 0,
				},

				form: {
								"trade_name":  '', // 商品名称
										"seller_account": 0, // 卖家账号
										"purchase_quantity":  0, // 购买数量
										"price":  '', // 价格
										"total_amount":  '', // 总金额
										"user_number": 0, // 用户编号
										"customized_requirements":  '', // 定制要求
										"related_pictures":  '', // 相关图片
										"completion_time":  '', // 完成时间
										"relevant_attachments":  '', // 相关附件
										"customized_video":  '', // 定制视频
										"customize_audio":  '', // 定制音频
										"required_date":  '', // 要求日期
										"custom_category":  '', // 定制类别
										"customization_details":  '', // 定制详情
										"picking_category":  '', // 取货类别
									"examine_state": "未审核",
								"i_want_to_customize_id": 0, // ID
								"seat": "", // 座位
				          			"user_id": this.$store.state.user.user_id,
	
				},
				disabledObj:{
								"trade_name_isDisabled": false,
										"seller_account_isDisabled": false,
					          			"purchase_quantity_isDisabled": false,
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
						// 用户组
				group_user_user_number: "",
				
		
		
		
		
		
		
						// 定制类别选项列表
				list_custom_category: [""],
	
		
						// 取货类别选项列表
				list_picking_category: ['送货上门','快递'],
	
	
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
                var json = await this.$get("~/api/user/get_list?user_group=卖家");
                if(json.result && json.result.list){
                    this.list_user_seller_account = json.result.list;
                }
                else if(json.error){
                    console.error(json.error);
                }
			},
					get_user_seller_account(id){
				var obj = this.list_user_seller_account.getObj({"user_id":id});
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
			
	
			
	
			
	
										set_total_amount(){
				this.form.total_amount = parseFloat(this.form.purchase_quantity) * parseFloat(this.form.price)
			},
							
	
				/**
			 * 获取商城用户用户列表
			 */
			async get_list_user_user_number() {
                var json = await this.$get("~/api/user/get_list?user_group=商城用户");
                if(json.result && json.result.list){
                    this.list_user_user_number = json.result.list;
                }
                else if(json.error){
                    console.error(json.error);
                }
			},
					/**
			 * 获取商城用户用户组
			 */
			async get_group_user_user_number() {
							this.form["user_number"] = this.$store.state.user.user_id;
							var json = await this.$get("~/api/user_group/get_obj?name=商城用户");
				if(json.result && json.result.obj){
					this.group_user_user_number = json.result.obj;
				}
				else if(json.error){
					console.error(json.error);
				}
			},
			get_user_session_user_number(id){
				var _this = this;
				var user_id = {"user_id":id}
				var url = "~/api/"+_this.group_user_user_number.source_table+"/get_obj?"
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
												_this.form["user_number"] = id
									_this.disabledObj['user_number' + '_isDisabled'] = true
						for (var i=0;i<arr.length;i++){
						  if (arr[i]!=='examine_state' && arr[i]!=='examine_reply') {
							for (var j = 0; j < arrForm.length; j++) {
							  if (arr[i] === arrForm[j]) {
								if (arr[i] !== "user_number") {
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
					get_user_user_number(id){
				var obj = this.list_user_user_number.getObj({"user_id":id});
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
			 * 上传相关图片
			 * @param {Object} param 图片参数
			 */
			upload_related_pictures(param){
						this.uploadFile(param.file, "related_pictures");
					},
	
	
			
	
						/**
			 * 上传相关附件
			 * @param {Object} param 文件参数
			 */
			upload_relevant_attachments(param){
						this.uploadFile(param.file, "relevant_attachments");
					},
	
	
						/**
			 * 上传定制视频
			 * @param {Object} param 视频参数
			 */
			upload_customized_video(param){
						this.uploadFile(param.file, "customized_video");
					},
	
	
						/**
			 * 上传定制音频
			 * @param {Object} param 音频参数
			 */
			upload_customize_audio(param){
						this.uploadFile(param.file, "customize_audio");
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
																	        if (this.form["completion_time"].indexOf("-")===-1){
            this.form["completion_time"] = this.$toTime(parseInt(this.form["completion_time"]),"yyyy-MM-dd hh:mm:ss")
        }
										        if (this.form["required_date"].indexOf("-")===-1){
          this.form["required_date"] = this.$toTime(parseInt(this.form["required_date"]),"yyyy-MM-dd")
        }
											$.db.del("form");

				this.get_list();
				return param;
			},

			/**
			 * 获取对象之后
			 * @param {Object} json
			 * @param {Object} func
			 */
			get_obj_after(json, func){


																									        if(this.form["completion_time"]=="0000-00-00 00:00:00"){
          this.form["completion_time"] = null;
        }
				if(parseInt(this.form["completion_time"]) > 9999){
					this.form["completion_time"] = this.$toTime(parseInt(this.form["completion_time"]),"yyyy-MM-dd hh:mm:ss")
				}
														        if(this.form["required_date"]=="0000-00-00"){
          this.form["required_date"] = null;
        }
				if(parseInt(this.form["required_date"]) > 9999){
					this.form["required_date"] = this.$toTime(parseInt(this.form["required_date"]),"yyyy-MM-dd")
				}
											


				this.get_list();
			},

			/**
			 * 提交前验证事件
			 * @param {Object} 请求参数
			 * @return {String} 验证成功返回null, 失败返回错误提示
			 */
			submit_check(param) {
				let msg = null
					if(this.act_limit_times>=this.limit_times){
					msg = "已超过提交次数";
				}
																																																						return msg;
			},

			is_view(){
				var bl = this.user_group == "管理员";

				if(!bl){
					bl = this.$check_action('/i_want_to_customize/table','add');
					console.log(bl ? "你有表格添加权限视作有添加权限" : "你没有表格添加权限");
				}
				if(!bl){
					bl = this.$check_action('/i_want_to_customize/table','set');
					console.log(bl ? "你有表格添加权限视作有修改权限" : "你没有表格修改权限");
				}
				if(!bl){
					bl = this.$check_action('/i_want_to_customize/view','add');
					console.log(bl ? "你有视图添加权限视作有添加权限" : "你没有视图添加权限");
				}
				if(!bl){
					bl = this.$check_action('/i_want_to_customize/view','set');
					console.log(bl ? "你有视图修改权限视作有修改权限" : "你没有视图修改权限");
				}
				if(!bl){
					bl = this.$check_action('/i_want_to_customize/view','get');
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
			  let seat = this.form.seat;
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
			 * 获取所有座位
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
														this.get_list_user_user_number();
					this.get_group_user_user_number();
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

	.seat-wrapper {
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
