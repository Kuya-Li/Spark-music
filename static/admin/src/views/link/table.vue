<template>
	<el-main class="bg table_wrap link">
		<el-form label-position="right" :model="query" class="form p_4" label-width="120">
			<el-row class="rows row1">
				<el-col :xs="24" :sm="12" :lg="8" class="el_form_search_wrap">
					<el-form-item label="链接名称">
						<el-input v-model="query.name"></el-input>
					</el-form-item>
				</el-col>
			</el-row>
			<el-row class="rows row2">
				<el-col :xs="24" :sm="24" :lg="24" class="search_btn_wrap">
					<el-col :xs="24" :sm="12" :lg="12" class="search_btn_1 btns">
						
							<el-button type="primary" @click="search()" class="search_btn_find">查询</el-button>
							<el-button @click="reset()" class="search_btn_reset">重置</el-button>
							<el-button v-if="user_group == '管理员' || $check_action('/link/table','del')" class="float-right search_btn_del" type="danger" @click="delInfo()">删除</el-button>
							<!-- <router-link v-if="user_group == '管理员' || $check_action('/link/view')" class="el-button float-right el-button--default el-button--primary search_btn_add"
								to="./view?"><span>添加</span>
							</router-link> -->
							<el-button  v-if="user_group == '管理员' || $check_action('/link/view')" class="float-right  search_btn_add" @click="$router.push('./view?')">添加</el-button>
					
					</el-col>
					
				</el-col>

			</el-row>
		</el-form>

		<el-table border :data="list" @selection-change="selectionChange" @sort-change="$sortChange" style="width: 100%" stripe>

			<el-table-column fixed type="selection" tooltip-effect="dark" width="55">
			</el-table-column>

			<el-table-column prop="img" label="友情链接图">
				<template slot-scope="scope">
					<div class="demo-image__preview">
						<el-image style="width: 100px; height: 100px" :src="$fullUrl(scope.row.img)" :preview-src-list="[$fullUrl(scope.row.img)]">
							<div slot="error" class="image-slot">
								<img src="../../../public/img/bg.jpg" style="width: 90px; height: 90px" />
							</div>
						</el-image>
					</div>
				</template>
			</el-table-column>

			<el-table-column prop="name" label="链接名称" sortable>
				<template slot-scope="scope">
					<a :href="scope.row.url">
						{{scope.row.name}}
					</a>
				</template>
			</el-table-column>

			<el-table-column prop="url" label="链接名" sortable>
			</el-table-column>

			<el-table-column prop="display" label="显示顺序" sortable>
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

			<!-- 操作 -->
			<el-table-column fixed="right" label="操作" width="80">
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
			<el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="query.page"
			 :page-sizes="[7, 10, 30, 100]" :page-size="query.size" layout="total, sizes, prev, pager, next, jumper" :total="count">
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

				field:"link_id",

				// 获取连接地址
				url_get_list: "~/api/link/get_list?like=0",
				url_del: "~/api/link/del?",

				// 查询
				query: {
					size: 10,
					page: 1,
					name: "",
				},

				// 数据
				list: [],
			}
		},
		methods:{
			table_class({row, column, rowIndex, columnIndex}){
				return "table_class";
			}
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

	.float-right {
		float: right;
	}

	.mr-1 {
		margin-right: 1rem;
	}

	.el-table .table_class {
		background: rgba(150, 150, 150, 0.1);
		text-align: center;
	}

	.text_center {
		text-align: center;
	}

	.float-right {
		float: right;
	}
</style>
