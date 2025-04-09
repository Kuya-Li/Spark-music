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
							<!-- 我要定制 -->
							<div><span>我要定制</span></div>
							<view_i_want_to_customize v-if="$check_action('/i_want_to_customize/table','get')"></view_i_want_to_customize>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>


<script>
	import list_admin_menu_user from "@/components/diy/list_admin_menu_user.vue";
	import view_i_want_to_customize from "../../components/diy/view_i_want_to_customize.vue";
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
			view_i_want_to_customize,
		},
	};
</script>

<style scoped>
	.container {
		min-height: 800px;
	}
</style>
