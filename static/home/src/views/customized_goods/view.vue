<template>
	<div class="page_user" id="user_address">
		<div class="warp">
			<div class="container">
				<div class="row justify-content-between">
					<div class="col-12 col-md-3">
						<div class="card_menu">
							<!-- 左侧边栏 -->
							<list_admin_menu_user></list_admin_menu_user>
						</div>
					</div>
					<div class="col-12 col-md-9">
						<div class="card_address pl-2">
							<!-- 定制商品 -->
							<div><span>定制商品</span></div>
							<view_customized_goods v-if="$check_action('/customized_goods/table','get')"></view_customized_goods>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>


<script>
	import list_admin_menu_user from "@/components/diy/list_admin_menu_user.vue";
	import view_customized_goods from "../../components/diy/view_customized_goods.vue";
	export default {
		data() {
			return {
			};
		},
		mounted() {
		},
		methods: {
		},
		components: {
			list_admin_menu_user,
			view_customized_goods,
		},
	};
</script>

<style scoped>
	.container {
		min-height: 800px;
	}
</style>
