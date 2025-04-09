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
							<!-- 商城用户 -->
							<div><span>商城用户</span></div>
							<table_mall_users v-if="$check_action('/mall_users/table','get')"></table_mall_users>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>


<script>
	import list_admin_menu_user from "@/components/diy/list_admin_menu_user.vue";
	import table_mall_users from "../../components/diy/table_mall_users.vue";
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
			table_mall_users,
		},
	};
</script>

<style scoped>
	.container {
		min-height: 800px;
	}
</style>
