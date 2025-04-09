<template>
	<div class="diy_list page_i_want_to_customize" id="i_want_to_customize_list">
		<div class="warp">
			<div class="container diy_list_container">
				<div class="diy_list_title">
					<div class="col">
						<span class="title">我要定制列表</span>
					</div>
				</div>
				<div class="row diy_list_search">
					<div class="col">
						<!-- 搜索栏 -->
						<div class="view">
							<span class="diy_list_search_title">关键字搜索：</span>
																					<b-form-input size="sm" class="mr-sm-2" placeholder="定制类别搜索" v-model="query['custom_category']" />
										<b-button size="sm" @click="search()" >
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
																								<b-dropdown text="定制类别" variant="outline-dark" left>
									<b-dropdown-item @click="filter_set('全部','custom_category')">全部</b-dropdown-item>
										<b-dropdown-item v-for="(o, i) in list_custom_category" :key="i" @click="filter_set(o['custom_category'],'custom_category')" >
												{{ o['custom_category'] }}
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
						<!-- 列表 -->
						<list_i_want_to_customize :list="list" />
						<!-- /列表 -->
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
	import list_i_want_to_customize from "@/components/diy/list_i_want_to_customize.vue";
	import diy_pager from "@/components/diy/diy_pager";
	import mixin from "@/mixins/page.js";

	export default {
		mixins: [mixin],
		components: {
			diy_pager,
			list_i_want_to_customize
		},
		data() {
			return {
				url_get_list: "~/api/i_want_to_customize/get_list?like=0",

				// 查询条件
				query: {
					keyword: "",
					page: 1,
					size: 10,
																					"custom_category": "", // 定制类别
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
						name: "定制类别正序",
						value: "custom_category asc",
					},
					{
						name: "定制类别倒序",
						value: "custom_category desc",
					},
							],

																															// 定制类别列表
				"list_custom_category": [""],
									// 取货类别列表
				"list_picking_category": ['送货上门','快递'],
		
			}
		},
		methods: {
      get_list_before(param) {
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


																	/**
			 * 获取定制类别列表
			 */
			async get_list_custom_category() {
				var json = await this.$get("~/api/classification_information/get_list?");
				if (json.result) {
					this.list_custom_category = json.result.list;
				} else if (json.error) {
					console.log(json.error);
				}
			},
			
			/**
			 * 筛选
			 */
																			filter_custom_category(o) {
				if (o == "全部") {
					this.query["custom_category"] = "";
				} else {
					this.query["custom_category"] = o;
				}
				this.search();
			},
										/**
			 * 重置
			 */
			reset() {
																				this.query.custom_category = ""
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

		},
		computed: {
		},
		created() {
																														/**
			 * 获取定制类别列表
			 */
			this.get_list_custom_category();
								}
	}
</script>

<style>
</style>
