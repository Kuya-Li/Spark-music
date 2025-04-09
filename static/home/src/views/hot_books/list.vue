<template>
	<div class="diy_list page_hot_books" id="hot_books_list">
		<div class="warp">
			<div class="container diy_list_container">
				<div class="diy_list_title">
					<div class="col">
						<span class="title">热卖图书列表</span>
					</div>
				</div>
				<div class="row diy_list_search">
					<div class="col">
						<!-- 搜索栏 -->
						<div class="view">
							<span class="diy_list_search_title">关键字搜索：</span>
									<b-form-input size="sm" class="mr-sm-2" placeholder="图书名称搜索" v-model="query['book_name']" />
										<b-form-input size="sm" class="mr-sm-2" placeholder="作者搜索" v-model="query['author']" />
									<b-form-input size="sm" class="mr-sm-2" placeholder="商品类别搜索" v-model="query['commodity_category']" />
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
																					<b-dropdown text="商品类别" variant="outline-dark" left>
									<b-dropdown-item @click="filter_set('全部','commodity_category')">全部</b-dropdown-item>
										<b-dropdown-item v-for="(o, i) in list_commodity_category" :key="i" @click="filter_set(o['commodity_category'],'commodity_category')" >
												{{ o['commodity_category'] }}
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
						<list_hot_books :list="list" />
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
	import list_hot_books from "@/components/diy/list_hot_books.vue";
	import diy_pager from "@/components/diy/diy_pager";
	import mixin from "@/mixins/page.js";

	export default {
		mixins: [mixin],
		components: {
			diy_pager,
			list_hot_books
		},
		data() {
			return {
				url_get_list: "~/api/hot_books/get_list?like=0",

				// 查询条件
				query: {
					keyword: "",
					page: 1,
					size: 10,
									"book_name": "", // 图书名称
												"author": "", // 作者
											"commodity_category": "", // 商品类别
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
						name: "图书名称正序",
						value: "book_name asc",
					},
					{
						name: "图书名称倒序",
						value: "book_name desc",
					},
								{
						name: "作者正序",
						value: "author asc",
					},
					{
						name: "作者倒序",
						value: "author desc",
					},
							{
						name: "商品类别正序",
						value: "commodity_category asc",
					},
					{
						name: "商品类别倒序",
						value: "commodity_category desc",
					},
								],

													// 商品类别列表
				"list_commodity_category": [""],
								
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
			 * 获取商品类别列表
			 */
			async get_list_commodity_category() {
				var json = await this.$get("~/api/classification_information/get_list?");
				if (json.result) {
					this.list_commodity_category = json.result.list;
				} else if (json.error) {
					console.log(json.error);
				}
			},
				
			/**
			 * 筛选
			 */
																				filter_commodity_category(o) {
				if (o == "全部") {
					this.query["commodity_category"] = "";
				} else {
					this.query["commodity_category"] = o;
				}
				this.search();
			},
											/**
			 * 重置
			 */
			reset() {
								this.query.book_name = ""
											this.query.author = ""
										this.query.commodity_category = ""
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
			 * 获取商品类别列表
			 */
			this.get_list_commodity_category();
										}
	}
</script>

<style>
</style>
