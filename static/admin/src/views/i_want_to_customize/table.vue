<template>
	<el-main class="bg table_wrap comtabel_t">
		<el-form label-position="right" :model="query" class="form p_4" label-width="120">
			<el-row class="rows row1">
			


																																														<el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
					<el-form-item label="定制类别">
									<el-select v-model="query.custom_category">
											<el-option v-for="o in list_custom_category" :key="o.custom_category" :label="o.custom_category"
								:value="o.custom_category">
							</el-option>
										</el-select>
								</el-form-item>
				</el-col>
													<el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
					<el-form-item label="审核状态">
						<el-select v-model="query.examine_state">
							<el-option value="">全部</el-option>
							<el-option value="未审核">未审核</el-option>
							<el-option value="已通过">已通过</el-option>
							<el-option value="未通过">未通过</el-option>
						</el-select>
					</el-form-item>
				</el-col>
				<el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
					<el-form-item label="支付状态">
						<el-select v-model="query.pay_state">
							<el-option value="">全部</el-option>
							<el-option value="未支付">未支付</el-option>
							<el-option value="已支付">已支付</el-option>
						</el-select>
					</el-form-item>
				</el-col>
			
	</el-row>
	<el-row class="rows row2">

		<el-col :xs="24" :sm="24" :lg="24" class="search_btn_wrap search_btns">
	
				<el-col :xs="24" :sm="10" :lg="8" class="search_btn_1 search_btn_wrap_1 btns">
					
										<el-button type="primary" @click="search()" class="search_btn_find">查询</el-button>
						<el-button @click="reset()" style="margin-right: 74px;" class="search_btn_reset">重置</el-button>
																		            		
						
						<el-button v-if="user_group == '管理员' || $check_action('/i_want_to_customize/table','del') || $check_action('/i_want_to_customize/view','del')" class="search_btn_del" type="danger" @click="delInfo()">删除</el-button>
									
				</el-col>
		</el-col>
	</el-row >
		
		</el-form>
		<el-table :data="list" @selection-change="selectionChange" @sort-change="$sortChange" style="width: 100%" id="dataTable">
			<el-table-column fixed type="selection" tooltip-effect="dark" width="55">
			</el-table-column>
				<el-table-column prop="trade_name" @sort-change="$sortChange" label="商品名称"
				v-if="user_group == '管理员' || $check_field('get','trade_name')" min-width="200">
					</el-table-column>
					<el-table-column prop="seller_account" @sort-change="$sortChange" label="卖家账号"
				v-if="user_group == '管理员' || $check_field('get','seller_account')" min-width="200">
						<template slot-scope="scope">
					{{ get_user_seller_account(scope.row['seller_account']) }}
				</template>
					</el-table-column>
					<el-table-column prop="purchase_quantity" @sort-change="$sortChange" label="购买数量"
				v-if="user_group == '管理员' || $check_field('get','purchase_quantity')" min-width="200">
					</el-table-column>
					<el-table-column prop="price" @sort-change="$sortChange" label="价格"
				v-if="user_group == '管理员' || $check_field('get','price')" min-width="200">
					</el-table-column>
					<el-table-column prop="total_amount" @sort-change="$sortChange" label="总金额"
				v-if="user_group == '管理员' || $check_field('get','total_amount')" min-width="200">
					</el-table-column>
					<el-table-column prop="user_number" @sort-change="$sortChange" label="用户编号"
				v-if="user_group == '管理员' || $check_field('get','user_number')" min-width="200">
						<template slot-scope="scope">
					{{ get_user_user_number(scope.row['user_number']) }}
				</template>
					</el-table-column>
					<el-table-column prop="customized_requirements" @sort-change="$sortChange" label="定制要求"
				v-if="user_group == '管理员' || $check_field('get','customized_requirements')" min-width="200">
					</el-table-column>
					<el-table-column prop="related_pictures" @sort-change="$sortChange" label="相关图片"
				v-if="user_group == '管理员' || $check_field('get','related_pictures')" min-width="200">
						<template slot-scope="scope">
					<el-image style="width: 100px; height: 100px" :src="$fullUrl(scope.row['related_pictures'])"
						:preview-src-list="[$fullUrl(scope.row['related_pictures'])]">
						<div slot="error" class="image-slot">
							<img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
						</div>
					</el-image>
				</template>
					</el-table-column>
					<el-table-column prop="completion_time" @sort-change="$sortChange" label="完成时间"
				v-if="user_group == '管理员' || $check_field('get','completion_time')" min-width="200">
						<template slot-scope="scope">
					{{ $toTime(scope.row["completion_time"],"yyyy-MM-dd hh:mm:ss") }}
				</template>
					</el-table-column>
					<el-table-column prop="relevant_attachments" @sort-change="$sortChange" label="相关附件"
				v-if="user_group == '管理员' || $check_field('get','relevant_attachments')" min-width="200">
						<template slot-scope="scope">
					<a :href="$fullUrl(scope.row['relevant_attachments'])" target="_blank" style="color: rgb(64, 158, 255);">点击下载</a>
				</template>
					</el-table-column>
					<el-table-column prop="customized_video" @sort-change="$sortChange" label="定制视频"
				v-if="user_group == '管理员' || $check_field('get','customized_video')" min-width="200">
						<template slot-scope="scope">
					<a href="javascript:void(0)" @click="customized_videoVideoPlay($fullUrl(scope.row['customized_video']))" >点此播放</a>
				</template>
					</el-table-column>
					<el-table-column prop="customize_audio" @sort-change="$sortChange" label="定制音频"
				v-if="user_group == '管理员' || $check_field('get','customize_audio')" min-width="200">
						<template slot-scope="scope">
					<a href="javascript:void(0)" @click="customize_audioAudioPlay($fullUrl(scope.row['customize_audio']))" >点此播放</a>
				</template>
					</el-table-column>
					<el-table-column prop="required_date" @sort-change="$sortChange" label="要求日期"
				v-if="user_group == '管理员' || $check_field('get','required_date')" min-width="200">
		                <template slot-scope="scope">
                	{{ $toTime(scope.row["required_date"],"yyyy-MM-dd") }}
                </template>
					</el-table-column>
					<el-table-column prop="custom_category" @sort-change="$sortChange" label="定制类别"
				v-if="user_group == '管理员' || $check_field('get','custom_category')" min-width="200">
					</el-table-column>
							<el-table-column prop="picking_category" @sort-change="$sortChange" label="取货类别"
				v-if="user_group == '管理员' || $check_field('get','picking_category')" min-width="200">
					</el-table-column>
	
			<el-table-column label="审核状态" prop="examine_state">
			</el-table-column>


			<el-table-column label="支付状态" prop="pay_state">
			</el-table-column>

			<el-table-column label="支付类型" prop="pay_type">
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


			<el-table-column
			prop="seat"	label="座位" v-if="user_group == '管理员' || $check_field('get', 'seat')"	min-width="200">
			</el-table-column>





			<el-table-column fixed="right" label="操作" min-width="200" v-if="user_group == '管理员' || $check_action('/i_want_to_customize/table','set') || $check_action('/i_want_to_customize/view','set') || $check_action('/i_want_to_customize/view','get') || $check_action('//table','add') || $check_action('//view','add')" >


				<template slot-scope="scope">
					<div class="view_a">
					<router-link class="e-button el-button--small is-plain el-button--success" style="margin: 5px !important;"
					v-if="user_group == '管理员' || $check_action('/i_want_to_customize/table','set') || $check_action('/i_want_to_customize/view','set') || $check_action('/i_want_to_customize/view','get')"
						:to="'./view?' + field + '=' + scope.row[field]"
						 size="small">
						<span>详情</span>
					</router-link>
					<el-button class="e-button el-button--small is-plain el-button--default" style="margin: 5px !important;" size="small" @click="openPayModal(scope.row)" v-if="scope.row.pay_state==='未支付' && (user_group == '管理员' || $check_pay('/i_want_to_customize/table'))">
						<span>支付</span>
					</el-button>
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
					title="视频详情"
					:visible.sync="customized_videoPlayerModalVisible"
					width="30%"
			>
				<video id="customized_videoPlayer" :src="customized_videoVideoUrl" autoplay="autoplay" width="100%" controls>
					您的浏览器不支持Video标签。
				</video>
				<span slot="footer" class="dialog-footer">
				<el-button @click="customized_videoCancelModalVisible">取 消</el-button>
				</span>
			</el-dialog>
					<el-dialog
					title="音频详情"
					:visible.sync="customize_audioAudioPlayerModalVisible"
					width="30%"
			>
				<audio id="customize_audioAudioPlayer" :src="customize_audioAudioUrl" autoplay="autoplay" width="100%" controls>
					您的浏览器不支持Audio标签。
				</audio>
				<span slot="footer" class="dialog-footer">
					<el-button @click="customize_audioCancelAudioModalVisible">取 消</el-button>
					</span>
			</el-dialog>
							<el-dialog
				title="支付"
				:visible.sync="payModalVisible"
				width="500px"
		>
			<el-tabs v-model="pay_obj.payActiveName" :stretch="true">
				<el-tab-pane label="微信" name="微信">
					<div style="width: 80%;margin: 0 auto;">
						<div style="width: 60%;margin: 30px auto;">
							<el-image style="width: 100%;" :src="$fullUrl('/static/img/wx.png')"
									  :preview-src-list="[$fullUrl('/static/img/wx.png')]">
								<div slot="error" class="image-slot">
									<img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
								</div>
							</el-image>
						</div>
						<div style="width: 80%;margin: 0 auto;">
							<div style="width: 100%;background-color: #409EFF;color: white;font-size: 14px;text-align: center;line-height: 40px;cursor: pointer" @click="submitPay()">确认支付</div>
						</div>
					</div>
				</el-tab-pane>
				<el-tab-pane label="支付宝" name="支付宝">
					<div style="width: 80%;margin: 0 auto;">
						<div style="width: 60%;margin: 30px auto;">
							<el-image style="width: 100%;" :src="$fullUrl('/static/img/aplipay.png')"
									  :preview-src-list="[$fullUrl('/static/img/aplipay.png')]">
								<div slot="error" class="image-slot">
									<img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
								</div>
							</el-image>
						</div>
						<div style="width: 80%;margin: 0 auto;">
							<div style="width: 100%;background-color: #409EFF;color: white;font-size: 14px;text-align: center;line-height: 40px;cursor: pointer" @click="submitPay()">确认支付</div>
						</div>
					</div>
				</el-tab-pane>
				<el-tab-pane label="网银" name="网银">
					<div style="width: 80%;margin: 0 auto;margin-top: 30px;">
						<div style="width: 80%;margin: 0 auto;">
							<div style="line-height: 40px">请输入网银账号：</div>
						</div>
						<div style="width: 80%;margin: 0 auto;">
							<el-input v-model="pay_obj.account" placeholder="请输入网银账号"></el-input>
						</div>
					</div>
					<div style="width: 80%;margin: 0 auto;margin-top: 20px;">
						<div style="width: 80%;margin: 0 auto;">
							<div style="line-height: 40px">请输入支付密码，6位数字：</div>
						</div>
						<div style="width: 80%;margin: 0 auto;">
							<el-input placeholder="请输入密码" v-model="pay_obj.password" show-password maxlength="6"></el-input>
						</div>
					</div>
					<div style="width: 80%;margin: 0 auto;margin-top: 40px;">
						<div style="width: 100%;background-color: #409EFF;color: white;font-size: 14px;text-align: center;line-height: 40px;cursor: pointer" @click="submitPay()">确认支付</div>
					</div>
				</el-tab-pane>
			</el-tabs>
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
				url_get_list: "~/api/i_want_to_customize/get_list?like=0",
				url_del: "~/api/i_want_to_customize/del?",

				// 字段ID
				field: "i_want_to_customize_id",

				// 查询
				query: {
					"size": 7,
					"page": 1,
																					"custom_category": "",
										"examine_state":"",
					"pay_state":"",
					"login_time": "",
					"create_time": "",
					"orderby": `create_time desc`
				},

				// 数据
				list: [],
				payModalVisible:false,
				pay_obj:{
					payActiveName:"微信",
					account:"",
					password:"",
					id:""
				},
															customized_videoPlayerModalVisible:false,
				customized_videoVideoUrl:"",
						customize_audioAudioPlayerModalVisible:false,
				customize_audioAudioUrl:"",
															// 用户列表
				list_user_seller_account: [],
															// 用户列表
				list_user_user_number: [],
																				// 定制类别列表
				list_custom_category: [""],
									}
		},
		methods: {
			// 关闭弹框
			closeModal(){
				this.showModal = false;
				},

			get_list_before(param){
				var user_group = this.user.user_group;
				if(user_group != "管理员"){
						switch(user_group){
																case "卖家":
							param["seller_account"] = this.user.user_id;
							break;
																													case "商城用户":
							param["user_number"] = this.user.user_id;
							break;
																																																												}
					}
				return param;
			},

																														/**
			 * 获取定制类别列表
			 */
			async get_list_custom_category() {
				var json = await this.$get("~/api/classification_information/get_list?");
				if(json.result){
					this.list_custom_category = json.result.list;
				}else if (json.error){
					console.log(json.error);
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
					ret = obj.nickname+"-"+obj.username;
					// if(obj.nickname){
					// 	ret = obj.nickname;
					// }
					// else{
					// 	ret = obj.username;
					// }
				}
				return ret;
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

			get_user_user_number(id){
				var obj = this.list_user_user_number.getObj({"user_id":id});
				var ret = "";
				if(obj){
					ret = obj.nickname+"-"+obj.username;
					// if(obj.nickname){
					// 	ret = obj.nickname;
					// }
					// else{
					// 	ret = obj.username;
					// }
				}
				return ret;
			},
															customized_videoVideoPlay(v) {
				this.customized_videoVideoUrl = v
				this.customized_videoPlayerModalVisible = true
			},

			customized_videoCancelModalVisible(){
				this.customized_videoVideoUrl = ""
				this.customized_videoPlayerModalVisible = false
			},
						customize_audioAudioPlay(v) {
				this.customize_audioAudioUrl = v
				this.customize_audioAudioPlayerModalVisible = true
			},

			customize_audioCancelAudioModalVisible(){
				this.customize_audioAudioUrl = ""
				this.customize_audioAudioPlayerModalVisible = false
			},
												openPayModal(v){
				this.pay_obj.id = v.i_want_to_customize_id
				this.payModalVisible = true
			},
			submitPay(){
				let _this = this;
				let url = this.$toUrl(this.query, "~/api/i_want_to_customize/set?i_want_to_customize_id="+this.pay_obj.id);
				let param = {"pay_state":"已支付","pay_type":this.pay_obj.payActiveName}
				this.$post(url, param, function(json, status) {
					console.log("提交结果：" ,json);
					if (json.result) {
						_this.$toast('支付成功！', 'success');
						_this.payModalVisible = false;
						_this.get_list();
					} else if (json.error) {
						_this.$toast(json.error.message, 'danger');
					}
				});
			},
			deleteRow(index, rows) {
				rows.splice(index, 1);
			}

		},
		created() {
									this.get_list_user_seller_account();
														this.get_list_user_user_number();
																			// 初始化定制类别列表
			this.get_list_custom_category();
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
