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
							<!-- 网站公告 -->
							<div><span>网站公告</span></div>
							<view_website_announcement v-if="$check_action('/website_announcement/table','get')"></view_website_announcement>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>


<script>
	import list_admin_menu_user from "@/components/diy/list_admin_menu_user.vue";
	import view_website_announcement from "../../components/diy/view_website_announcement.vue";
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
			view_website_announcement,
		},
	};
</script>

<style scoped>
	.container {
		min-height: 800px;
	}
</style>
