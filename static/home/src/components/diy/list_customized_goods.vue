<template>
	<div class="diy_home diy_list diy_customized_goods" id="diy_customized_goods_list">
		<!-- 列表 -->
		<div class="diy_view_list list list-x" v-if="show">
			<router-link class="diy_card goods diy_list_box_wrap" v-for="(o, i) in list" :key="i"
				:to="'/customized_goods/details?customized_goods_id=' + o['customized_goods_id']">
				<!-- 图片 -->
				<div class="diy_list_img_box" v-if="imgList.length" >
					<div class="diy_row" v-for="(item,index) in imgList" :key="item+index" v-show="$check_field('get',item.name,'/customized_goods/details') && +item.is_img_list">
						<div class="diy_title diy_list_img_title">
							<span>{{item.title}}:</span>
						</div>
						<div class="diy_field diy_img">
							<img :src="$fullUrl(o[item.name])" style="width:100%;height:100%" />
						</div>
					</div>
				</div>
				<!-- 内容 -->
				<div class="diy_list_item_box">
					<div class="diy_list_item_content" v-for="(item,index) in showItemList" :key="item+index">
						<div class="diy_row" :class="{[item.name]:true}" v-if="$check_field('get',item.name,'/customized_goods/details') && +item.is_img_list">
							<div class="diy_title">
								<span>{{item.title}}:</span>
							</div>
							<div class="diy_field diy_text">
								<span v-if="item.type == 'UID'" v-text="get_user_name(item.name,o[item.name])"></span>
								<span v-else-if="item.type == '日期'" v-text="$toTime(o[item.name],'yyyy-MM-dd')"></span>
								<span v-else-if="item.type == '时间'" v-text="$toTime(o[item.name],'hh:mm:ss')"></span>
								<span v-else-if="item.type == '日长'" v-text="$toTime(o[item.name],'yyyy-MM-dd hh:mm:ss')"></span>
								<span v-else v-text="o[item.name]"></span>
							</div>
						</div>
					</div>
				</div>
			</router-link>
		</div>




		<!-- 表格 -->
		<div class="diy_view_table" v-else>
			<table class="diy_table">
				<tr class="diy_row">
						<th class="diy_title" v-if="$check_field('get','trade_name')">
						商品名称
					</th>
							<th class="diy_title" v-if="$check_field('get','stock')">
						库存
					</th>
									<th class="diy_title" v-if="$check_field('get','picture')">
						图片
					</th>
											<th class="diy_title" v-if="$check_field('get','remarks')">
						备注
					</th>
							<th class="diy_title" v-if="$check_field('get','seller_account')">
						卖家账号
					</th>
							<th class="diy_title" v-if="$check_field('get','product_category')">
						商品类别
					</th>
							<th class="diy_title" v-if="$check_field('get','price')">
						价格
					</th>
									<th class="diy_title" v-if="$check_field('get','production_time')">
						生产时间
					</th>
							<th class="diy_title" v-if="$check_field('get','date')">
						日期
					</th>
							<th class="diy_title" v-if="$check_field('get','special_price_or_not')">
						是否特价
					</th>
							<th class="diy_title" v-if="$check_field('get','category')">
						类别
					</th>
							<th class="diy_title" v-if="$check_field('get','customized_categories')">
						定制类别
					</th>
					</tr>
				<tr class="diy_row" v-for="(o,i) in list" :key="o+i">
						<td class="diy_field diy_text" v-if="$check_field('get','trade_name')">
						<span>
							{{ o["trade_name"] }}
						</span>
					</td>
							<td class="diy_field diy_number" v-if="$check_field('get','stock')">
						<span>
							{{ o["stock"] }}
						</span>
					</td>
									<td class="diy_field" v-if="$check_field('get','picture')">
						<img class="diy_img" :src="o['picture']" />
					</td>
											<td class="diy_field diy_text" v-if="$check_field('get','remarks')">
						<span>
							{{ o["remarks"] }}
						</span>
					</td>
							<td class="diy_field diy_uid" v-if="$check_field('get','seller_account')">
						<span>
							{{ get_user_name('seller_account',o['seller_account']) }}
						</span>
					</td>
							<td class="diy_field diy_text" v-if="$check_field('get','product_category')">
						<span>
							{{ o["product_category"] }}
						</span>
					</td>
							<td class="diy_field diy_number" v-if="$check_field('get','price')">
						<span>
							{{ o["price"] }}
						</span>
					</td>
									<td class="diy_field diy_datetime" v-if="$check_field('get','production_time')">
						<span>
							{{ $toTime(o["production_time"] ,"yyyy-MM-dd hh:mm:ss") }}
						</span>
					</td>
							<td class="diy_field diy_date" v-if="$check_field('get','date')">
						<span>
							{{ $toTime(o["date"] ,"yyyy-MM-dd") }}
						</span>
					</td>
							<td class="diy_field diy_text" v-if="$check_field('get','special_price_or_not')">
						<span>
							{{ o["special_price_or_not"] }}
						</span>
					</td>
							<td class="diy_field diy_text" v-if="$check_field('get','category')">
						<span>
							{{ o["category"] }}
						</span>
					</td>
							<td class="diy_field diy_text" v-if="$check_field('get','customized_categories')">
						<span>
							{{ o["customized_categories"] }}
						</span>
					</td>
					</tr>
			</table>
		</div>
		<!-- 轮播 -->

		 <div class="carousel ins_s">
                <div class="slider" ref="slider">
                <div  v-for="(o, i) in  list" :key="i" class="slide" >
                    
                    <router-link :to="'/customized_goods/details?customized_goods_id=' + o['customized_goods_id']" class="lis_cont">
                        <div class="diy_list_img_box" v-if="imgList.length" >
    					        <div class="diy_row" v-for="(item, index) in imgList" :key="item + index" v-show="$check_field('get',item.name,'/customized_goods/details') && +item.is_img_list">
    						<div class="diy_title diy_list_img_title">
							
    						</div>
    						<div class="diy_field diy_img">
    							<img :src="$fullUrl(o[item.name])" style="width:100%;height:100%" />
    						</div>
                      
    					</div>
                        </div>
                           
                    <div class="context">
                        <div class="diy_list_item_content" v-for="(item,index) in showItemList" :key="item+index">
						<div class="diy_row" :class="{[item.name]:true}"  v-if="$check_field('get',item.name,'/customized_goods/details') && +item.is_img_list">
							<div class="diy_title">
								<span>{{item.title}}:</span>
							</div>
							<div class="diy_field diy_text">
								<span v-if="item.type == 'UID'" v-text="get_user_name(item.name,o[item.name])"></span>
								<span v-else-if="item.type == '日期'" v-text="$toTime(o[item.name],'yyyy-MM-dd')"></span>
								<span v-else-if="item.type == '时间'" v-text="$toTime(o[item.name],'hh:mm:ss')"></span>
								<span v-else-if="item.type == '日长'" v-text="$toTime(o[item.name],'yyyy-MM-dd hh:mm:ss')"></span>
								<span v-else v-text="o[item.name]"></span>
							</div>
						</div>
					</div>
                             
                    </div>
                </router-link>
                </div>
                </div>
                <button class="prev" @click="prevSlide">&lt;</button>
                <button class="next" @click="nextSlide">&gt;</button>
            </div>
			<div class="pagination" >
				<button v-for="page in pagarr" :key="page" @click="handleButtonClick(page)" :class="{ pag_btn:page, active: page === activePage }">{{ page }}</button>
 		 	</div>

	</div>
</template>

<script>
	export default {
		props: {
			list: {
				type: Array,
				default: function() {
					return [];
				},
			},
			show: {
				type: Boolean,
				default: function(){
					return true;
				}
			}
		},
		data() {
			return {
				 translateX: 0,
                currentIndex: 0,	
                timer: null,
				pagarr:[1,2,3,4],
				activePage: 1,
				currentPage: 1,
      			itemsPerPage: 3,
				totalItems: 3,
						imgList: [
						{
							title: "图片",
							name: "picture",
							type: "图片",
							is_img_list: "1"
						},
						],
						itemList: [
								{
									title: "商品名称",
									name: "trade_name",
									type: "文本",
									is_img_list: "1"
								},
								{
									title: "库存",
									name: "stock",
									type: "数字",
									is_img_list: "1"
								},
								{
									title: "附件",
									name: "enclosure",
									type: "文件",
									is_img_list: "0"
								},
								{
									title: "视频",
									name: "video",
									type: "视频",
									is_img_list: "0"
								},
								{
									title: "音频",
									name: "audio_frequency",
									type: "音频",
									is_img_list: "0"
								},
								{
									title: "卖家账号",
									name: "seller_account",
									type: "UID",
									is_img_list: "0"
								},
								{
									title: "商品类别",
									name: "product_category",
									type: "下选",
									is_img_list: "0"
								},
								{
									title: "价格",
									name: "price",
									type: "数字",
									is_img_list: "1"
								},
								{
									title: "生产时间",
									name: "production_time",
									type: "日长",
									is_img_list: "0"
								},
								{
									title: "日期",
									name: "date",
									type: "日期",
									is_img_list: "0"
								},
								{
									title: "是否特价",
									name: "special_price_or_not",
									type: "下拉",
									is_img_list: "0"
								},
								{
									title: "类别",
									name: "category",
									type: "下随",
									is_img_list: "0"
								},
								{
									title: "定制类别",
									name: "customized_categories",
									type: "下随",
									is_img_list: "0"
								},
						],
						richList: [
								{
									title: "备注",
									name: "remarks",
									type: "多文本"
								},
								{
									title: "详情",
									name: "details",
									type: "编辑"
								},
						],
												// 用户列表
				list_user_seller_account: [],
												};
		},
		methods: {
			/**
			 * 添加购物车
			 */
			 	 handleButtonClick(index){

				this.activePage = index;
				if (index == 1  ) {
					
					this.translateX = -this.currentIndex * 0;

				}
				if (index == 2  ) {

					this.translateX = -99.99;
					
				}

				if(index == 3 ){
					this.translateX = -199.98
				}
				if(index == 4){
					this.translateX = -299.96999999999997
					
				}
				this.$nextTick(() => {
							this.$refs.slider.classList.add('slide-transition');
							
							this.$refs.slider.style.transform = `translateX(${this.translateX}%)`;
						});
				},

				prevSlide() {

				if (this.currentIndex === 0) {
					this.currentIndex = this.$props.list.length - 3;
				} else {
					this.currentIndex--;
				}
				this.translateX = -this.currentIndex * 33.33;

				this.$nextTick(() => {
							this.$refs.slider.classList.add('slide-transition');
							if (this.currentIndex ==9) {
								this.$refs.slider.classList.remove('slide-transition');
							}
							this.$refs.slider.style.transform = `translateX(${this.translateX}%)`;
						});

				},
				nextSlide() {

					if (this.currentIndex===8) {
						this.$refs.slider.classList.remove('slide-transition');
					}
					if ( this.currentIndex === this.$props.list.length - 3) {
						
						this.currentIndex = 0
						
					} else {
						this.currentIndex++;
					}

					this.translateX = -this.currentIndex * 33.33;
					
						this.$nextTick(() => {
							
							this.$refs.slider.classList.add('slide-transition');
							if (this.currentIndex ==0) {
								this.$refs.slider.classList.remove('slide-transition');
							}
							this.$refs.slider.style.transform = `translateX(${this.translateX}%)`;
					});

			},
			get_user_name(name,id){
				var obj = null;
												if (name == 'seller_account'){
					obj = this.list_user_seller_account.getObj({"user_id":id});
				}
													var ret = "";
				if(obj){
					ret = obj.nickname+"-"+obj.username;
					// if(obj.nickname){
					// 	ret = obj.nickname;
					// }
					// else{
					// 	ret = obj.username;
					// }
				}
				return ret;
			},
											/**
			 * 获取卖家用户列表
			 */
			async get_list_user_seller_account() {
				var json = await this.$get("~/api/user/get_list?user_group=卖家");
				if(json.result && json.result.list){
					this.list_user_seller_account = json.result.list;
				}
				else if(json.error){
					console.error(json.error);
				}
			},
											},
		created() {
											this.get_list_user_seller_account();
											},
		computed:{
			showItemList(){
				let arr = [];
				let _type = ["视频","音频","文件"];
				this.itemList.forEach(item => {
					if(_type.indexOf(item.type) === -1 && !!+item.is_img_list){
						arr.push(item)
					}
				})
				return arr.slice(0,4);
			}
		}
	};
</script>

<style scoped>
	.media {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		flex-basis: 75%;
		min-height: 10rem;
	}

	.goods {
		display: flex;
		width: calc(25% - 1rem);
		margin: 0.5rem;
		padding: 0.5rem;
		flex-direction: column;
		justify-content: space-between;
		background-color: white;
		border-radius: 0.5rem;
	}

	.goods:hover {
		border: 0.2rem solid #909399;
		box-shadow: 0 0.1rem 0.3rem rgba(0, 0, 0, 0.15);
	}

	.goods:hover img {
		filter: blur(1px);
	}

	.price {
		font-size: 1rem;
		margin-right: 3px;
	}

	.price_ago {
		text-decoration: line-through;
		font-size: 0.5rem;
		color: #999;

	}

	.title {
		word-break: break-all;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
		font-weight: 700;
		padding: .25rem;
	}

	.icon_cart {
		color: #FF5722;
		float: right;
	}

	@media (max-width: 992px) {

		.goods {
			width: calc(33% - 1rem);
			;
		}

	}

	@media (max-width: 768px) {

		.goods {
			width: calc(50% - 1rem);
			;
		}

	}
	
.slide-transition {
  transition: transform 0.5s ease;
}
    .carousel {
        position: relative;
        width: 100%;
        height: 300px; /* 设置轮播图的高度 */
        overflow: hidden;
        }

.slider {
  display: flex;

}

.slide {
    flex-shrink: 0;
	width: calc(33.33% - 1rem);
   
}


.slide img{
    width: 300px;
    height: 200px ;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.prev,
.next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 40px;
  font-size: 24px;
  background-color: #ccc;
  border-radius: 50%;
  border: none;
  color: #fff;
  opacity: 0.7;
}

.prev {
  left: 10px;
}

.next {
  right: 10px;
}

.pagination {
    display: flex;
    /* padding-left: 0; */
    /* list-style: none; */
    width: 20%;
    left: 41%;
    justify-content: space-around;
    font-size: 25px;
    border: none;
}

button.active {
  background-color: rgb(221, 127, 4);
  color: white;
}
</style>

