<template>
	<div>
			<el-form-item v-if="$check_register_field('add','seller_account_number','/seller/view')" label="卖家账号" prop="seller_account_number">
				<el-input id="seller_account_number" v-model="form['seller_account_number']" placeholder="请输入卖家账号"></el-input>
				</el-form-item>
				<el-form-item v-if="$check_register_field('add','store_name','/seller/view')" label="店铺名称" prop="store_name">
				<el-input id="store_name" v-model="form['store_name']" placeholder="请输入店铺名称"></el-input>
				</el-form-item>
	
	</div>
</template>

<script>
	import mixin from "@/mixins/component.js";

	export default {
		mixins: [mixin],
		props:{

			form:{
				type: Object,
				default: function(){
					return {
							"seller_account_number":  '' ,
								"store_name":  '' ,
						}
				}
			},

		},
		data() {
			return {
				field: "seller_id",
				url_add: "~/api/seller/add?",
				url_set: "~/api/seller/set?",
				url_upload: "~/api/seller/upload?",

						rules: {
					"seller_account_number": [    {required: true,message: '卖家账号不能为空'},  ],
					"store_name": [    {required: true,message: '店铺名称不能为空'},  ],
				}

			}
		},
		methods: {

	
	
	

	
	
	

		},
		created() {
				}
	}
</script>
