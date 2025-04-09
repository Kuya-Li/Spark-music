<template>
  <el-main class="bg table_wrap">
    <el-form label-position="right" :model="query" class="form p_4" label-width="120">
      <el-row class="rows row1">

          
                                                              <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
                      <el-form-item label="商品名称">
                                                      <el-input v-model="query.trade_name"></el-input>
                                                </el-form-item>
                    </el-col>
                                                                                                                                                                                                                                                                                                      <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
                      <el-form-item label="商品类别">
                                                      <el-input v-model="query.product_category"></el-input>
                                                </el-form-item>
                    </el-col>
                                                                                                                                                                                                      <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
                      <el-form-item label="是否特价">
                                                      <el-select v-model="query.special_price_or_not">
                                                                  <el-option v-for="o in list_special_price_or_not" :key="o" :label="o"
                                             :value="o">
                                  </el-option>
                                                            </el-select>
                                                </el-form-item>
                    </el-col>
                                                                                                                            <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
            <el-form-item label="审核状态">
              <el-select v-model="query.examine_state">
                <el-option value="">全部</el-option>
                <el-option value="未审核">未审核</el-option>
                <el-option value="已通过">已通过</el-option>
                <el-option value="未通过">未通过</el-option>
              </el-select>
            </el-form-item>
          </el-col>
                      </el-row>
      <el-row class="rows row2">
      	<el-col :xs="24" :sm="24" :lg="24" class="search_btn_wrap search_btns">
         <el-col :xs="24" :sm="10" :lg="8" class="search_btn_1 search_btn_wrap_1 btns">
                              <el-button type="primary" @click="search()" class="search_btn_find">查询</el-button>
                <el-button @click="reset()" style="margin-right: 74px;" class="search_btn_reset">重置</el-button>
                                            <el-button v-if="$check_option('/customized_goods/table','export_db')" @click="export_db('dataTable')"  class="derive" style="margin-right: 155px;">导出</el-button>
                                            <el-button v-if="$check_option('/customized_goods/table','print')" @click="print('dataTable')" style="margin-right: 155px;" class="search_btn_print">打印</el-button>
                         
            <el-button v-if="user_group == '管理员' || $check_action('/customized_goods/table','add') || $check_action('/customized_goods/view','add')" @click="$router.push('./view?')" class="add">添加</el-button>
						
            <el-button v-if="user_group == '管理员' || $check_action('/customized_goods/table','del') || $check_action('/customized_goods/view','del')" class="search_btn_del" type="danger" @click="delInfo()">删除</el-button>
                        </el-col>
       
        </el-col>
      </el-row>
    </el-form>
    <el-table :data="list" @selection-change="selectionChange" @sort-change="$sortChange" style="width: 100%" id="dataTable">
                <el-table-column type="selection" tooltip-effect="dark" width="55">
            </el-table-column>
                                                  <el-table-column prop="trade_name" @sort-change="$sortChange" label="商品名称"
                               v-if="user_group == '管理员' || $check_field('get','trade_name')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="stock" @sort-change="$sortChange" label="库存"
                               v-if="user_group == '管理员' || $check_field('get','stock')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="enclosure" @sort-change="$sortChange" label="附件"
                               v-if="user_group == '管理员' || $check_field('get','enclosure')" min-width="200">
                                      <template slot-scope="scope">
                      <a :href="$fullUrl(scope.row['enclosure'])" target="_blank" style="color: rgb(64, 158, 255);">点击下载</a>
                    </template>
                                </el-table-column>
                                              <el-table-column prop="picture" @sort-change="$sortChange" label="图片"
                               v-if="user_group == '管理员' || $check_field('get','picture')" min-width="200">
                                      <template slot-scope="scope">
                      <el-image style="width: 100px; height: 100px" :src="$fullUrl(scope.row['picture'])"
                                :preview-src-list="[$fullUrl(scope.row['picture'])]">
                        <div slot="error" class="image-slot">
                          <img src="../../../public/img/error.png" style="width: 90px; height: 90px" />
                        </div>
                      </el-image>
                    </template>
                                </el-table-column>
                                              <el-table-column prop="video" @sort-change="$sortChange" label="视频"
                               v-if="user_group == '管理员' || $check_field('get','video')" min-width="200">
                                      <template slot-scope="scope">
                      <a href="javascript:void(0)" @click="videoVideoPlay($fullUrl(scope.row['video']))" >点此播放</a>
                    </template>
                                </el-table-column>
                                              <el-table-column prop="audio_frequency" @sort-change="$sortChange" label="音频"
                               v-if="user_group == '管理员' || $check_field('get','audio_frequency')" min-width="200">
                                      <template slot-scope="scope">
                      <a href="javascript:void(0)" @click="audio_frequencyAudioPlay($fullUrl(scope.row['audio_frequency']))" >点此播放</a>
                    </template>
                                </el-table-column>
                                              <el-table-column prop="remarks" @sort-change="$sortChange" label="备注"
                               v-if="user_group == '管理员' || $check_field('get','remarks')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="seller_account" @sort-change="$sortChange" label="卖家账号"
                               v-if="user_group == '管理员' || $check_field('get','seller_account')" min-width="200">
                                      <template slot-scope="scope">
                      {{ get_user_seller_account(scope.row['seller_account']) }}
                    </template>
                                </el-table-column>
                                              <el-table-column prop="product_category" @sort-change="$sortChange" label="商品类别"
                               v-if="user_group == '管理员' || $check_field('get','product_category')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="price" @sort-change="$sortChange" label="价格"
                               v-if="user_group == '管理员' || $check_field('get','price')" min-width="200">
                                </el-table-column>
                                                                              <el-table-column prop="production_time" @sort-change="$sortChange" label="生产时间"
                               v-if="user_group == '管理员' || $check_field('get','production_time')" min-width="200">
                                      <template slot-scope="scope">
                      {{ $toTime(scope.row["production_time"],"yyyy-MM-dd hh:mm:ss") }}
                    </template>
                                </el-table-column>
                                              <el-table-column prop="date" @sort-change="$sortChange" label="日期"
                               v-if="user_group == '管理员' || $check_field('get','date')" min-width="200">
                                      <template slot-scope="scope">
                      {{ $toTime(scope.row["date"],"yyyy-MM-dd") }}
                    </template>
                                </el-table-column>
                                              <el-table-column prop="special_price_or_not" @sort-change="$sortChange" label="是否特价"
                               v-if="user_group == '管理员' || $check_field('get','special_price_or_not')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="category" @sort-change="$sortChange" label="类别"
                               v-if="user_group == '管理员' || $check_field('get','category')" min-width="200">
                                </el-table-column>
                                              <el-table-column prop="customized_categories" @sort-change="$sortChange" label="定制类别"
                               v-if="user_group == '管理员' || $check_field('get','customized_categories')" min-width="200">
                                </el-table-column>
                    
                  <el-table-column label="审核状态" prop="examine_state">
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

                  <el-table-column prop="qrcode_title" label="二维码标题"
                           v-if="user_group == '管理员' || $check_field('get','qrcode_title')" min-width="200">
          </el-table-column>
          <el-table-column prop="qrcode_img" label="二维码图片"
                           v-if="user_group == '管理员' || $check_field('get','qrcode_img')" min-width="200">
            <template slot-scope="scope">
              <el-popover placement="right" trigger="hover">
                <img :src="$fullUrl(scope.row['qrcode_img'])" style="width:300px;height:450px;"/>
                <img slot="reference" :src="$fullUrl(scope.row['qrcode_img'])"  style="max-width: 100px;max-height: 100px">
              </el-popover>
            </template>
          </el-table-column>
        
        
                  <el-table-column prop="timer_title" label="计时器标题"
                           v-if="user_group == '管理员' || $check_field('get','timer_title')" min-width="200">
          </el-table-column>
          <el-table-column sortable prop="timing_start_time" label="计时开始时间" min-width="200">
            <template slot-scope="scope">
              {{ $toTime(scope.row["timing_start_time"],"yyyy-MM-dd hh:mm:ss") }}
            </template>
          </el-table-column>
          <el-table-column sortable prop="timing_end_time" label="计时结束时间" min-width="200">
            <template slot-scope="scope">
              {{ $toTime(scope.row["timing_end_time"],"yyyy-MM-dd hh:mm:ss") }}
            </template>
          </el-table-column>
        
                  <el-table-column sortable prop="location_address" label="当前位置" min-width="200">
          </el-table-column>
        
                  <el-table-column
              prop="limit_times"	label="限制次数" v-if="user_group == '管理员' || $check_field('get', 'limit_times')"	min-width="200">
          </el-table-column>
        

                <el-table-column label="操作" min-width="120" v-if="user_group == '管理员' || $check_action('/customized_goods/table','set') || $check_action('/customized_goods/view','set') || $check_action('/customized_goods/view','get') || $check_action('/定制/table','add') || $check_action('/定制/view','add')" >
        

      <template slot-scope="scope">
        <router-link class="el-button el-button--small is-plain el-button--success" style="margin: 5px !important;"
                     v-if="user_group == '管理员' || $check_action('/customized_goods/table','set') || $check_action('/customized_goods/view','set') || $check_action('/customized_goods/view','get')"
                                 :to="'./view?' + field + '=' + scope.row[field]"
                                 size="small">
          <span>详情</span>
        </router-link>
                                        <!--跨表按钮-->
                                      <el-button class="el-button el-button--small is-plain el-button--default" style="margin: 5px !important;" size="small" @click="to_table(scope.row,'/i_want_to_customize/view')" v-if="user_group == '管理员' || $check_action('/i_want_to_customize/table','add') || $check_action('/i_want_to_customize/view','add')">
                      <span>定制</span>
                    </el-button>
                                                                                                      <router-link v-if="user_group == '管理员' || $check_comment('/customized_goods/table')" class="el-button el-button--small is-plain el-button--primary"
                             :to="'../comment/table?size=10&page=1&source_table=customized_goods&source_field=' + field + '&source_id=' + scope.row[field]" size="small">
                  查看评论
                </router-link>
                              </template>
    </el-table-column>

    </el-table>

    <!-- 分页器 -->
    <div class="mt text_center">
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
                     :current-page="query.page" :page-sizes="[7, 10, 30, 100]" :page-size="query.size"
                     layout="total, sizes, prev, pager, next, jumper" :total="count">
      </el-pagination>
    </div>
    <!-- /分页器 -->

                                                                                            <el-dialog
                title="视频详情"
                :visible.sync="videoPlayerModalVisible"
                width="30%"
            >
              <video id="videoPlayer" :src="videoVideoUrl" autoplay="autoplay" width="100%" controls>
                您的浏览器不支持Video标签。
              </video>
              <span slot="footer" class="dialog-footer">
				<el-button @click="videoCancelModalVisible">取 消</el-button>
				</span>
            </el-dialog>
                                      <el-dialog
                title="音频详情"
                :visible.sync="audio_frequencyAudioPlayerModalVisible"
                width="30%"
            >
              <audio id="audio_frequencyAudioPlayer" :src="audio_frequencyAudioUrl" autoplay="autoplay" width="100%" controls>
                您的浏览器不支持Audio标签。
              </audio>
              <span slot="footer" class="dialog-footer">
					<el-button @click="audio_frequencyCancelAudioModalVisible">取 消</el-button>
					</span>
            </el-dialog>
                                                                                                                                                                                            
    <div class="modal_wrap" v-if="showModal">
      <div class="modal_box">
        <!-- <div class="modal_box_close" @click="closeModal">X</div> -->
        <p class="modal_box_title">重要提醒</p>
        <p class="modal_box_text">当前有数据达到预警值！</p>
        <div class="btn_box">
          <span @click="closeModal">取消</span>
          <span @click="closeModal">确定</span>
        </div>
      </div>
    </div>


  </el-main>
</template>
<script>
  import mixin from "@/mixins/page.js";
  
  export default {
    mixins: [mixin],
    data() {
      return {
        // 弹框
        showModal: false,
        // 获取数据地址
        url_get_list: "~/api/customized_goods/get_list?like=0",
        url_del: "~/api/customized_goods/del?",

        // 字段ID
        field: "customized_goods_id",

        // 查询
        query: {
          "size": 7,
          "page": 1,
                                                                      "trade_name": "",
                                                                                                                                                                                                                                                                                                              "product_category": "",
                                                                                                                                                                                                                          "special_price_or_not": "",
                                                                                                                            "examine_state":"",
                                          "login_time": "",
          "create_time": "",
          "orderby": `create_time desc`
        },

                  // 数据
        list: [],
                                                                                                                                                                            videoPlayerModalVisible:false,
                      videoVideoUrl:"",
                                                            audio_frequencyAudioPlayerModalVisible:false,
                      audio_frequencyAudioUrl:"",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          // 用户列表
                list_user_seller_account: [],
                                                                                                                                                                                                                                                    // 是否特价列表
                list_special_price_or_not: ['是','否'],
                                                                                                                        }
    },
    methods: {
      // 关闭弹框
      closeModal(){
        this.showModal = false;
      },
                
                  get_list_before(param){
            var user_group = this.$store.state.user.user_group;
            if(user_group != "管理员"){
                                  switch(user_group){
                                                                                                                                                                                                                                                                                                                                                                                                                            case "卖家":
                              param["seller_account"] = this.$store.state.user.user_id;
                              break;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                  }
                            }
            return param;
          },
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                  /**
           * 导出
           */
          export_db(tableid){
            // var query = this.query;
            // this.$get("~/api/customized_goods/export_db?",query,(json)=>{
            // 	if(json.result){
            // 		console.log(json.result);
            // 	}else if(json.error){
            // 		console.error(json.error);
            // 	}
            // });


            //导出表格
            var idTmr;

            function getExplorer() {
              var explorer = window.navigator.userAgent;
              //ie
              if(explorer.indexOf("MSIE") >= 0) {
                return 'ie';
              }
              //firefox
              else if(explorer.indexOf("Firefox") >= 0) {
                return 'Firefox';
              }
              //Chrome
              else if(explorer.indexOf("Chrome") >= 0) {
                return 'Chrome';
              }
              //Opera
              else if(explorer.indexOf("Opera") >= 0) {
                return 'Opera';
              }
              //Safari
              else if(explorer.indexOf("Safari") >= 0) {
                return 'Safari';
              }
            }
            function Cleanup() {
              window.clearInterval(idTmr);
              CollectGarbage();
            }
            var tableToExcel = (function() {
              var uri = 'data:application/vnd.ms-excel;base64,',
                  template = '<html><head><meta charset="UTF-8"></head><body><table  border="1">{table}</table></body></html>',
                  base64 = function(
                      s) {
                    return window.btoa(unescape(encodeURIComponent(s)))
                  },
                  format = function(s, c) {
                    return s.replace(/{(\w+)}/g, function(m, p) {
                      return c[p];
                    })
                  }
              return function(table, name) {
                if(!table.nodeType)
                  table = document.getElementById(table)
                var ctx = {
                  worksheet: name || 'Worksheet',
                  table: table.innerHTML
                }
                window.location.href = uri + base64(format(template, ctx))
              }
            })();
            if(getExplorer() == 'ie') {
              var curTbl = document.getElementById(tableid);
              var oXL = new ActiveXObject("Excel.Application");
              var oWB = oXL.Workbooks.Add();
              var xlsheet = oWB.Worksheets(1);
              var sel = document.body.createTextRange();
              sel.moveToElementText(curTbl);
              sel.select();
              sel.execCommand("Copy");
              xlsheet.Paste();
              oXL.Visible = true;

              try {
                var fname = oXL.Application.GetSaveAsFilename("Excel.xls",
                    "Excel Spreadsheets (*.xls), *.xls");
              } catch(e) {
                print("Nested catch caught " + e);
              } finally {
                oWB.SaveAs(fname);
                oWB.Close(savechanges = false);
                oXL.Quit();
                oXL = null;
                idTmr = window.setInterval("Cleanup();", 1);
              }

            } else {
              tableToExcel(tableid)
            }


          },
        
        
          /**
           * 打印开始
           */
          print(tableid){

            //	打印表格
            var win = window.open('');

            var tableToPrintA = document.getElementById(tableid);
            win.document.write(tableToPrintA.outerHTML);
            win.document.write('</div></body></html>');
            win.document.close();
            win.focus();
            win.print();
            win.close();
          },

          /**
           *
           * 打印结束
           *
           * **/

        
        
                                                                                                                                                                                    videoVideoPlay(v) {
                this.videoVideoUrl = v
                this.videoPlayerModalVisible = true
              },

                    videoCancelModalVisible(){
                this.videoVideoUrl = ""
                this.videoPlayerModalVisible = false
              },
                                                                audio_frequencyAudioPlay(v) {
                this.audio_frequencyAudioUrl = v
                this.audio_frequencyAudioPlayerModalVisible = true
              },

                    audio_frequencyCancelAudioModalVisible(){
                this.audio_frequencyAudioUrl = ""
                this.audio_frequencyAudioPlayerModalVisible = false
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

              get_user_seller_account(id){
                var obj = this.list_user_seller_account.getObj({"user_id":id});
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
                                                                                                                                                                                                                                                                                                                              deleteRow(index, rows) {
        rows.splice(index, 1);
      }

    },
    created() {
                                                                                                                                                                                                                                                                                                      this.get_list_user_seller_account();
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

  .text_center {
    text-align: center;
  }

  .float-right {
    float: right;
  }


  .modal_wrap{
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    background: rgba(0,0,0,0.5);
    z-index: 9999999999;
  }
  .modal_wrap .modal_box{
    width: 400px;
    height: 200px;
    background: url("../../assets/modal_bg.jpg") no-repeat center;
    background-size: cover;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -200px;
    margin-top: -100px;
    border-radius: 10px;
  }
  .modal_wrap .modal_box .modal_box_close{
    font-size: 20px;
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
  }
  .modal_wrap .modal_box .modal_box_title{
    text-align: center;
    font-size: 18px;
    margin: 16px auto;
    color: #fff;
    border-bottom: 1px solid rgba(117, 116, 116,0.5);
    padding-bottom: 16px;
    width: 356px;
  }
  .modal_wrap .modal_box .modal_box_text{
    text-align: center;
    font-size: 15px;
    color: #fff;
    margin-top: 25px;
  }
  .modal_wrap .modal_box .btn_box{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-top: 42px;
  }
  .modal_wrap .modal_box .btn_box span{
    display: inline-block;
    width: 80px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    border: 1px solid #ccc;
    font-size: 14px;
    cursor: pointer;
    color: #fff;
  }
  .modal_wrap .modal_box .btn_box span:nth-child(2){
    background: #409EFF;
    color: #fff;
    border-color: #409EFF;
    margin-left: 15px;
  }
</style>
