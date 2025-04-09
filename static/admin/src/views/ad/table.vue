<template>
	<el-main class="bg table_wrap ad">
		<el-form label-position="right" :model="query" class="form p_4" label-width="120">
			<el-row class="rows row1">
				<el-col :xs="24" :sm="12" :lg="6" class="el_form_search_wrap">
					<el-form-item label="标题">
						<el-input v-model="query.title"></el-input>
					</el-form-item>
				</el-col>
				<el-col :xs="24" :sm="12" :lg="6" class="el_form_search_wrap">
					<el-form-item label="投放位置">
						<el-select v-model="query.location" placeholder="请选择">
							<el-option value="顶部广告">顶部广告</el-option>
							<el-option value="中部广告">中部广告</el-option>
							<el-option value="底部广告">底部广告</el-option>
						</el-select>
					</el-form-item>
				</el-col>
			</el-row>
			<el-row class="rows row2">
				<el-col :xs="24" :sm="24" :lg="24" class="search_btn_wrap btns">
					<el-col :xs="24" :sm="12" :lg="12" class="search_btn_1 btns">
						<el-button type="primary" @click="search()" class="search_btn_find">查询</el-button>
						<el-button @click="reset()" class="search_btn_reset">重置</el-button>
						<el-button v-if="user_group == '管理员' || $check_action('/ad/table','del')" class="float-right search_btn_del" type="danger" @click="delInfo()">删除</el-button>
						<el-button  v-if="user_group == '管理员' || $check_action('/ad/view')" class="float-right  search_btn_add" @click="$router.push('./view?')">添加</el-button>
					</el-col>

				</el-col>
			</el-row>
		</el-form>

		<el-table :data="list" @selection-change="selectionChange" @sort-change="$sortChange" style="width: 100%"
			border>
			<!-- 多选按钮 -->
			<el-table-column fixed type="selection" tooltip-effect="dark" width="55">
			</el-table-column>
			<!-- /多选按钮 -->

<!--			<el-table-column label="封面图" v-if="$check_field('get','img')" prop="img" min-width="110">-->
<!--				<template slot-scope="scope">-->
<!--					<el-image style="width: 100px; height: 100px" :src="$fullUrl(scope.row.img)"-->
<!--						:preview-src-list="[$fullUrl(scope.row.img)]">-->
<!--						<div slot="error" class="image-slot">-->
<!--							<img src="/img/error.png" style="width: 100px; height: 100px" />-->
<!--						</div>-->
<!--					</el-image>-->
<!--				</template>-->
<!--			</el-table-column>-->

			<el-table-column sortable prop="title" label="标题" min-width="120">
			</el-table-column>

			<el-table-column prop="url" label="链接" min-width="100">
			</el-table-column>

<!--			<el-table-column sortable prop="hits" label="点击量" min-width="100">-->
<!--			</el-table-column>-->

<!--			<el-table-column sortable prop="display" label="显示顺序" min-width="100">-->
<!--			</el-table-column>-->

			<el-table-column sortable prop="location" label="投放位置" min-width="120">
			</el-table-column>

			<el-table-column sortable prop="create_time" label="创建时间" min-width="100">
				<template slot-scope="scope">
				    {{ $toTime(scope.row["create_time"],"yyyy-MM-dd hh:mm:ss") }}
				</template>
			</el-table-column>

			<el-table-column sortable prop="update_time" label="更新时间" min-width="100">
				<template slot-scope="scope">
				    {{ $toTime(scope.row["update_time"],"yyyy-MM-dd hh:mm:ss") }}
				</template>
			</el-table-column>

			<!-- 操作 -->
			<el-table-column fixed="right" label="操作" width="200">
				<template slot-scope="scope">
					<div class="view_a">
					<router-link class="e-button el-button--small is-plain el-button--primary"
						:to="'./view?' + field + '=' + scope.row[field]" size="small">
						<span>详情</span>
					</router-link>
				</div>
				</template>
			</el-table-column>
			<!-- /操作 -->

		</el-table>

		<!-- 分页器 -->
		<div class="mt text_center">
			<el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
				:current-page="query.page" :page-sizes="[7, 10, 30, 100]" :page-size="query.size"
				layout="total, sizes, prev, pager, next, jumper" :total="count">
			</el-pagination>
		</div>
		<!-- /分页器 -->

	</el-main>
</template>

<script>
	import mixin from "@/mixins/page.js";

	export default {
		mixins: [mixin],
		data() {
			return {
				table: "ad",
				field: "ad_id",
				url_get_list: "~/api/ad/get_list?like=0",
				url_del: "~/api/ad/del?",

				query: {
					size: 10,
					page: 1,
					name: ""
				},

				// 数据
				list: [],
			}
		},
		methods: {
			table_class({
				row,
				column,
				rowIndex,
				columnIndex
			}) {
				return "table_class";
			}

		},
		created() {
		}
	}
</script>

<style>

</style>
