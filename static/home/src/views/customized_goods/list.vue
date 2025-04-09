<template>
	<div class="diy_list page_customized_goods" id="customized_goods_list">
		<div class="warp">
			<div class="container diy_list_container">
				<div class="diy_list_title">
					<div class="col">
						<span class="title">定制商品列表</span>
					</div>
				</div>
				<div class="row diy_list_search">
					<div class="col">
						<!-- 搜索栏 -->
						<div class="view">
							<span class="diy_list_search_title">关键字搜索：</span>
								<b-form-input size="sm" class="mr-sm-2" placeholder="商品名称搜索" v-model="query['trade_name']" />
																<b-form-input size="sm" class="mr-sm-2" placeholder="商品类别搜索" v-model="query['product_category']" />
													<b-form-input size="sm" class="mr-sm-2" placeholder="是否特价搜索" v-model="query['special_price_or_not']" />
										<b-button size="sm" @click="search_customized_goods()" >
								<b-icon icon="search"/>
							</b-button>
						</div>
						<!-- /搜索栏 -->
					</div>
				</div>
				<div class="diy_list_select_box">
					<span class="diy_list_select_title">下拉搜索：</span>
						<div class="diy_list_dropdown_box">
						<div class="col">
							<!-- 筛选 -->
							<div class="view">
																														<b-dropdown text="是否特价" variant="outline-dark" left>
									<b-dropdown-item @click="filter_set('全部','special_price_or_not')">全部</b-dropdown-item>
										<b-dropdown-item v-for="(o,i) in list_special_price_or_not" @click="filter_set(o,'special_price_or_not')" >
										{{ o }}
										</b-dropdown-item>
								</b-dropdown>
												</div>
							<!-- /筛选 -->
						</div>
					</div>
					<div class="diy_list_sort_box">
						<div class="col">
							<!-- 排序 -->
							<div class="view">
								<b-dropdown text="排序" variant="outline-dark" left>
										<b-dropdown-item v-for="(o, i) in list_sort" :key="i" @click="set_sort(o)" >
												{{ o.name }}
										</b-dropdown-item>
								</b-dropdown>
							</div>
							<!--/排序 -->
						</div>
					</div>
				</div>

				<div class="row diy_list_box">
					<div class="col">
						<!-- tab -->
																																	<b-tabs content-class="mt-3">
							<b-tab v-for="(o, i) in list_type_product_category" :title="o['product_category']" :active="i===0" @click="tab_select(o['product_category'])">
								<div class="row">
									<div class="col">
										<!-- tab -->
										<list_customized_goods :list="type_list[o['product_category']]" />
										<!-- /tab -->
									</div>
								</div>
							</b-tab>
						</b-tabs>
																														<!-- /tab -->
					</div>
				</div>
				<div class="row diy_list_page_box">
					<div class="col overflow-auto flex_cc">
						<!-- 分页器 -->
<!--						<diy_pager v-model="query['page']" :size="query['size']" :count="count" v-on:toPage="toPage" v-on:toSize="toSize" ></diy_pager>-->
            <b-pagination
                v-model="query.page"
                :total-rows="count"
                :per-page="query.size"
                @change="goToPage"
            />
						<!-- /分页器 -->
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import list_customized_goods from "@/components/diy/list_customized_goods.vue";
	import diy_pager from "@/components/diy/diy_pager";
	import mixin from "@/mixins/page.js";

	export default {
		mixins: [mixin],
		components: {
			diy_pager,
			list_customized_goods
		},
		data() {
			return {
				url_get_list: "~/api/customized_goods/get_list?like=0",

				// 查询条件
				query: {
					keyword: "",
					page: 1,
					size: 10,
								"trade_name": "", // 商品名称
																		"product_category": "", // 商品类别
															"special_price_or_not": "", // 是否特价
										"examine_state": "已通过", // 审核状态
				},

				// 排序内容
				list_sort: [{
						name: "创建时间从高到低",
						value: "create_time desc",
					},
					{
						name: "创建时间从低到高",
						value: "create_time asc",
					},
					{
						name: "更新时间从高到低",
						value: "update_time desc",
					},
					{
						name: "更新时间从低到高",
						value: "update_time asc",
					},
						{
						name: "商品名称正序",
						value: "trade_name asc",
					},
					{
						name: "商品名称倒序",
						value: "trade_name desc",
					},
														{
						name: "商品类别正序",
						value: "product_category asc",
					},
					{
						name: "商品类别倒序",
						value: "product_category desc",
					},
											{
						name: "是否特价正序",
						value: "special_price_or_not asc",
					},
					{
						name: "是否特价倒序",
						value: "special_price_or_not desc",
					},
							],

																															// 是否特价列表
				"list_special_price_or_not": ['是','否'],
						
																															"list_type_product_category": [],
				"type_list":{},
																											}
		},
		methods: {
      get_list_before(param) {
        var oNowDate = this.dateFormat("yyyy-MM-dd hh:mm:ss")+"";
        var url_get_list = "~/api/customized_goods/get_list?timing_start_time_max=" + oNowDate +
            "&timing_end_time_min=" + oNowDate + "&like=0";
        this.url_get_list= url_get_list;
      },
			/**
			 * 筛选选择
			 */
			filter_set(o,key) {
			    if (o == "全部") {
			        this.query[key] = "";
			    } else {
			        this.query[key] = o;
			    }
			    this.search();
			},

			/**
			 * 排序
			 */
			set_sort(o) {
			    this.query.orderby = o.value;
			    this.search();
			},

																														async get_list_type_product_category() {
				var json = await this.$get("~/api/customized_goods/get_list?groupby=product_category"
										,{"examine_state": "已通过"}
				);
				if (json.result) {
					this.list_type_product_category = json.result.list;
					for (let i = 0;i<this.list_type_product_category.length;i++){
						this.get_product_category_type_list(this.list_type_product_category[i].product_category);
					}
					this.query.product_category = this.list_type_product_category[0].product_category;
					this.get_list();
				} else if (json.error) {
					console.log(json.error);
				}
			},

			get_product_category_type_list(type){
				let _this = this;
				this.$get("~/api/customized_goods/get_list?", {"product_category":type
									,"examine_state": "已通过"
								}, (json) => {
					if (json.result) {
						_this.$set(_this.type_list,type, json.result.list);
					}
				});
			},
			tab_select(v){
				this.query.product_category = v;
				this.get_list();
			},
			search_customized_goods(){
				let _this = this;
				this.$get("~/api/customized_goods/get_list?like=0", _this.query, (json) => {
					if (json.result) {
						_this.$set(_this.type_list,_this.query.product_category, json.result.list);
						_this.get_list();
					}
				});
			},
																								
																
			/**
			 * 筛选
			 */
																													filter_special_price_or_not(o) {
				if (o == "全部") {
					this.query["special_price_or_not"] = "";
				} else {
					this.query["special_price_or_not"] = o;
				}
				this.search();
			},
										/**
			 * 重置
			 */
			reset() {
							this.query.trade_name = ""
																	this.query.product_category = ""
														this.query.special_price_or_not = ""
									this.search();
			},

			// 返回条数
			toSize(i){
				this.query.size = i;
				this.first();
			},

			// 返回页数
			toPage(i){
				this.query.page = i;
				this.first();
			},

      goToPage(v){
        this.query.page = v;
        this.goToNew(v)
      },

			dateFormat(fmt) {
				var myDate = new Date();
				var o = {
					"M+": myDate.getMonth() + 1, // 月份
					"d+": myDate.getDate(), // 日
					"h+": myDate.getHours(), // 小时
					"m+": myDate.getMinutes(), // 分
					"s+": myDate.getSeconds(), // 秒
					"q+": Math.floor((myDate.getMonth() + 3) / 3), // 季度
					"S": myDate.getMilliseconds() // 毫秒
				};
				if (/(y+)/.test(fmt))
					fmt = fmt.replace(RegExp.$1, (myDate.getFullYear() + "").substr(4 - RegExp.$1.length));
				for (var k in o)
					if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
						return fmt;
			},
		},
		computed: {
		},
		created() {
																																																														this.get_list_type_product_category();
																										}
	}
</script>

<style>
</style>
