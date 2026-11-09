// VL_VERSION:4.3.0
// Preview: width:1920px height:1080px
<Section-Dashboard "root">

# Frontend Public Props

# Frontend Public Events

# Frontend Public Methods
// @meta method description:"Reload all dashboard data" returns:({success:{description:"Whether the call succeeded"}})
METHOD Refresh();RETURN {success:BOOL}
-init() -> _r
-RETURN {success:_r.success}

# Frontend Global Vars
$loaded(BOOL) = false
$activeTab(STRING) = "mid"
$orgStats([{label:STRING,value:INT,sortOrder:INT}]) = []
$memberDonut([{label:STRING,value:INT,color:STRING,showLegend:INT,sortOrder:INT}]) = []
$collegeRatios([{label:STRING,currentVal:INT,totalVal:INT,pctLabel:STRING,pctNum:INT,color:STRING,sortOrder:INT}]) = []
$incubationProjects([{title:STRING,level:STRING,sortOrder:INT}]) = []
$cadreTabs([{tabKey:STRING,label:STRING,sortOrder:INT}]) = []
$cadreGenders([{tabKey:STRING,label:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
$cadreAges([{tabKey:STRING,label:STRING,value:INT,pctNum:INT,color:STRING,sortOrder:INT}]) = []
$cadreTitles([{tabKey:STRING,label:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
$orgKpis([{label:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
$duesBars([{monthLabel:STRING,value:INT,sortOrder:INT}]) = []
$sideJobSlices([{label:STRING,value:INT,percent:STRING,color:STRING,sortOrder:INT}]) = []
$mediaRanks([{label:STRING,value:STRING,barPct:INT,sortOrder:INT}]) = []
$mediaTable([{platform:STRING,postCount:STRING,readCount:STRING,sortOrder:INT}]) = []
$studyBars([{label:STRING,annualVal:INT,monthlyVal:INT,sortOrder:INT}]) = []
$opinionAreas([{ageLabel:STRING,partyVal:INT,disciplineVal:INT,sortOrder:INT}]) = []
$warningSummaries([{groupKey:STRING,title:STRING,modelCount:INT,blueCount:INT,yellowCount:INT,redCount:INT,sortOrder:INT}]) = []
$warningBars([{groupKey:STRING,modelLabel:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
$majorEvent({totalCount:INT,doneCount:INT,pctLabel:STRING,pctNum:INT}) = {totalCount:0,doneCount:0,pctLabel:"",pctNum:0}
$platformMeta({schoolCn:STRING,schoolEn:STRING,title:STRING,sideJobTotal:INT}) = {schoolCn:"Lakeview University",schoolEn:"SMART CAMPUS · OPERATIONS CENTER",title:"Smart Campus Operations Dashboard",sideJobTotal:328}

# Frontend Tree
<ServiceDomain-Dashboard "dashboardSvc">
-<Service-GetDashboardData> params:() returns:(success(BOOL),message(STRING),orgStats([{}]),memberDonut([{}]),collegeRatios([{}]),incubationProjects([{}]),cadreTabs([{}]),cadreGenders([{}]),cadreAges([{}]),cadreTitles([{}]),orgKpis([{}]),duesBars([{}]),sideJobSlices([{}]),mediaRanks([{}]),mediaTable([{}]),studyBars([{}]),opinionAreas([{}]),warningSummaries([{}]),warningBars([{}]),majorEvent({}),platformMeta({}))

// ===== Responsive cockpit: vertical sizes/fonts in vh, widths in %, every 16:9 viewport (1920/1600/1366/1280) fits on one screen =====
<Col-PageShell> width:"100%" height:"100vh" overflow:"hidden" sk.bg:"#02060f" sk.bgImage:"radial-gradient(1200px 700px at 50% -10%, rgba(60,170,255,0.20), transparent 60%), radial-gradient(900px 600px at 8% 100%, rgba(30,100,200,0.18), transparent 60%), radial-gradient(900px 600px at 92% 100%, rgba(30,100,200,0.18), transparent 60%), linear-gradient(180deg, #04091f 0%, #02060f 70%)" font-family:"PingFang SC, Microsoft YaHei, sans-serif"
-<Col-DashboardBody> width:"100%" height:"100%" min-height:"0" padding:"8px 12px 11px"

// ========== HEADER ==========
--<Row-Header> width:"100%" height:"65px" min-height:"0" align-items:"center" justify-content:"space-between" padding:"0 14px" sk.borderBottom:"1px solid rgba(80,180,255,0.50)"
---<Row-Brand> width:"23%" align-items:"center" gap:"10px"
----<Col-Badge> width:"52px" height:"52px" sk.bgImage:"radial-gradient(circle, #0a2a55 0%, #04122c 70%)" sk.radius:"50%" sk.borderColor:"#22e1ff" sk.borderWidth:"2px" align-items:"center" justify-content:"center"
-----<Text-Univ> value:"LU" font-size:"13px" sk.fg:"#eaffff" font-weight:"700"
----<Col-Name> gap:"2px"
-----<Text-NameCn> value:$platformMeta.schoolCn font-size:"24px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"3px"
-----<Text-NameEn> value:$platformMeta.schoolEn font-size:"11px" sk.fg:"#7aa0c8" letter-spacing:"2px"
---<Row-TitleWrap> flex:"1" align-items:"center" justify-content:"center" gap:"14px"
----<Col-DecoL> flex:"1" min-width:"20px" height:"22px" sk.bgImage:"linear-gradient(90deg, transparent 0%, rgba(34,225,255,0.55) 30%, rgba(80,180,255,0.30) 100%)" sk.borderBottom:"1px solid rgba(80,180,255,0.45)"
----<Text-PlatformTitle> value:$platformMeta.title font-size:"33px" font-weight:"700" sk.fg:"#eaf6ff" letter-spacing:"6px" font-family:"Microsoft YaHei, sans-serif"
----<Col-DecoR> flex:"1" min-width:"20px" height:"22px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.30) 0%, rgba(34,225,255,0.55) 70%, transparent 100%)" sk.borderBottom:"1px solid rgba(80,180,255,0.45)"
---<Row-Meta> width:"23%" justify-content:"flex-end" gap:"14px" align-items:"baseline"
----<Text-Time> value:"20:08:58" font-size:"24px" sk.fg:"#eaf6ff" font-weight:"600" font-family:"Consolas, monospace" letter-spacing:"2px"
----<Text-Date> value:"2022/8/24" font-size:"16px" sk.fg:"#9ec6ee" font-family:"Consolas, monospace" letter-spacing:"1px"

// ========== GRID 3 COLUMNS — left 25% / mid 50% / right 25% ==========
--<Row-Grid> width:"100%" flex:"1" min-height:"0" gap:"9px" padding:"9px 0 0"

// ============ LEFT COLUMN (25%) ============
---<Col-Left> width:"25%" height:"100%" min-height:"0" gap:"8px"

// — Campus Population (flex 21) —
----<Col-PanelDangyuan> width:"100%" height:"216px" min-height:"0" padding:"8px 12px 11px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"5px"
-----<Row-TitleDangyuan> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
------<Text-TDangyuan> value:"Campus Population" font-size:"16px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
-----<Row-DangyuanBody> width:"100%" flex:"1" min-height:"0" gap:"8px"
------<Col-StatsCol> width:"22%" flex:"1" min-height:"0" gap:"5px" justify-content:"space-between"
-------<For-OrgStats> sourceArray:$orgStats loopVar:[_s,_si] // VL-FIXED-LIST-OK: reason="3 fixed KPI rows"
--------<Col-StatBox> width:"100%" flex:"1" min-height:"0" align-items:"center" justify-content:"center" padding:"3px 6px" sk.bgImage:"linear-gradient(180deg, rgba(60,160,255,0.22), rgba(20,60,140,0.06))" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" sk.borderLeft:"3px solid #22e1ff"
---------<Text-StatV> value:_s.value font-size:"26px" font-weight:"700" sk.fg:"#ffd23a" font-family:"Consolas, monospace" line-height:"1"
---------<Text-StatL> value:_s.label font-size:"11px" sk.fg:"#b9d8f5" letter-spacing:"1px"
------<Col-DonutWrap> width:"34%" align-items:"center" justify-content:"center" gap:"4px"
-------<Col-DonutPie> width:"92px" height:"92px" sk.radius:"50%" sk.bgImage:"conic-gradient(#25e8e0 0deg 245deg, #ff5aa8 245deg 320deg, #ffd23a 320deg 343deg, #b06bff 343deg 360deg)" align-items:"center" justify-content:"center"
--------<Col-DonutHole> width:"52px" height:"52px" sk.radius:"50%" sk.bg:"#04122c" align-items:"center" justify-content:"center"
---------<Text-DonutTotal> value:"9446" font-size:"15px" sk.fg:"#eaf6ff" font-weight:"700" font-family:"Consolas, monospace"
-------<Col-DonutLegend> width:"100%" gap:"2px"
--------<For-DonutLegend> sourceArray:$memberDonut loopVar:[_md,_mdi] // VL-FIXED-LIST-OK: reason="4 fixed slice legend items"
---------<Row-DLegRow> width:"100%" min-height:"14px" align-items:"center" gap:"4px"
----------<Col-DLegDot> width:"8px" height:"8px" sk.radius:"50%" sk.bg:_md.color
----------<Text-DLegL> value:_md.label font-size:"10px" sk.fg:"#cfe6ff" flex:"1" line-height:"1.2"
----------<Text-DLegV> value:_md.value font-size:"10px" sk.fg:"#fff" font-family:"Consolas, monospace" font-weight:"700"
------<Col-CollegeRatios> width:"44%" gap:"11px" justify-content:"center" padding:"2px 4px"
-------<For-CollegeRatios> sourceArray:$collegeRatios loopVar:[_c,_ci] // VL-FIXED-LIST-OK: reason="2 fixed progress bars"
--------<Col-CollegeRow> width:"100%" min-height:"41px" gap:"3px"
---------<Row-CollegeH> width:"100%" align-items:"center" gap:"4px"
----------<Icon-Caret> value:"f0da" fontSet:"fa-solid-900" font-size:"11px" sk.fg:"#22e1ff"
----------<Text-CollegeName> value:_c.label font-size:"12px" sk.fg:"#9fd4ff" letter-spacing:"1px"
---------<Row-CollegeVals> width:"100%" justify-content:"space-between" align-items:"baseline"
----------<Text-CollegeFrac> value:(_c.currentVal + " / " + _c.totalVal) font-size:"12px" sk.fg:"#d8ecff" font-family:"Consolas, monospace"
----------<Text-CollegePct> value:_c.pctLabel font-size:"14px" font-weight:"700" sk.fg:(_c.color == "green" ? "#2bf08a" : "#22e1ff") font-family:"Consolas, monospace"
---------<Row-CollegeBar> width:"100%" height:"6px" sk.bg:"rgba(80,180,255,0.10)" sk.borderColor:"rgba(80,180,255,0.25)" sk.borderWidth:"1px" overflow:"hidden"
----------<Col-CollegeFill> width:(_c.pctNum + "%") height:"100%" sk.bgImage:(_c.color == "green" ? "linear-gradient(90deg, #0d8a4a, #2bf08a)" : "linear-gradient(90deg, #0a8db0, #22e1ff)")

// — Campus Sites + Key Projects (flex 21) —
----<Row-MapProjects> width:"100%" height:"205px" min-height:"0" gap:"8px"
-----<Col-PanelMap> width:"48%" height:"100%" min-height:"0" padding:"8px 12px 11px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"5px"
------<Row-TitleMap> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
-------<Text-TMap> value:"Campus Sites" font-size:"15px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
------<Col-MapArea> width:"100%" flex:"1" min-height:"0" sk.bgImage:"radial-gradient(circle at 50% 45%, rgba(40,140,220,0.35), transparent 70%), linear-gradient(180deg, rgba(10,40,90,0.4), rgba(5,20,60,0.4))" sk.borderColor:"rgba(80,180,255,0.18)" sk.borderWidth:"1px" align-items:"center" justify-content:"center" gap:"4px" padding:"5px"
-------<Row-MapCities1> width:"100%" justify-content:"space-around" align-items:"center"
--------<Col-CityHzh> align-items:"center" gap:"2px"
---------<Col-CityDot1> width:"9px" height:"9px" sk.radius:"50%" sk.bg:"#22e1ff"
---------<Text-CityL1> value:"North Campus" font-size:"10px" sk.fg:"#cfe6ff"
--------<Col-CityHz> align-items:"center" gap:"2px"
---------<Col-CityDot2> width:"11px" height:"11px" sk.radius:"50%" sk.bg:"#2bf08a"
---------<Text-CityL2> value:"Main Campus" font-size:"11px" sk.fg:"#2bf08a" font-weight:"700"
--------<Col-CityWz> align-items:"center" gap:"2px"
---------<Col-CityDot3> width:"8px" height:"8px" sk.radius:"50%" sk.bg:"#22e1ff"
---------<Text-CityL3> value:"East Campus" font-size:"10px" sk.fg:"#cfe6ff"
-------<Row-MapCities2> width:"100%" justify-content:"space-around" align-items:"center" padding:"4px 0 0"
--------<Col-CityShx> align-items:"center" gap:"2px"
---------<Col-CityDot4> width:"8px" height:"8px" sk.radius:"50%" sk.bg:"#22e1ff"
---------<Text-CityL4> value:"Science Park" font-size:"10px" sk.fg:"#cfe6ff"
--------<Col-CityNb> align-items:"center" gap:"2px"
---------<Col-CityDot5> width:"8px" height:"8px" sk.radius:"50%" sk.bg:"#22e1ff"
---------<Text-CityL5> value:"Medical Center" font-size:"10px" sk.fg:"#cfe6ff"
-------<Text-MapTitle> value:"5 sites · 1 network" font-size:"11px" sk.fg:"rgba(207,230,255,0.5)" letter-spacing:"2px" padding:"4px 0 0"
-----<Col-PanelProjects> width:"50%" height:"100%" min-height:"0" padding:"8px 12px 11px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"5px"
------<Row-TitleProj> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
-------<Text-TProj> value:"Key Projects" font-size:"15px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
------<Col-ProjList> width:"100%" flex:"1" min-height:"0" overflow:"auto" gap:"4px" padding:"2px"
-------<For-Projects> sourceArray:$incubationProjects loopVar:[_p,_pi] // VL-FIXED-LIST-OK: reason="5 fixed projects"
--------<Row-ProjItem> width:"100%" flex:"1" min-height:"24px" align-items:"center" gap:"6px" padding:"3px 6px" sk.bg:"rgba(80,180,255,0.05)" sk.borderLeft:"1px solid rgba(80,180,255,0.30)"
---------<Col-ProjTag> padding:"2px 8px" sk.bgImage:(_p.level == "State" ? "linear-gradient(135deg, #8b46ff, #c46bff)" : "linear-gradient(135deg, #1f8bff, #5ad6ff)") align-items:"center" justify-content:"center" min-width:"36px"
----------<Text-TagL> value:_p.level font-size:"10px" sk.fg:"#fff" font-weight:"700" letter-spacing:"1px"
---------<Text-ProjTitle> value:_p.title font-size:"12px" sk.fg:"#dbeeff" flex:"1" line-height:"1.3"

// — Workforce Tabs (flex 24) —
----<Col-PanelCadre> width:"100%" height:"238px" min-height:"0" padding:"8px 12px 11px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"5px"
-----<Row-CadreTabs> width:"100%" align-items:"flex-end" gap:"0" sk.borderBottom:"1px solid rgba(80,180,255,0.30)"
------<For-CadreTabs> sourceArray:$cadreTabs loopVar:[_t,_ti] // VL-FIXED-LIST-OK: reason="3 fixed tab chips"
-------<Col-TabBtn "cadreTab"> padding:"6px 16px" min-height:"32px" sk.bgImage:($activeTab == _t.tabKey ? "linear-gradient(180deg, rgba(34,225,255,0.18), rgba(34,225,255,0.04))" : "none") sk.borderColor:($activeTab == _t.tabKey ? "rgba(80,180,255,0.30)" : "transparent") sk.borderWidth:"1px" sk.borderBottom:($activeTab == _t.tabKey ? "2px solid #22e1ff" : "0 solid transparent") align-items:"center" justify-content:"center" style:"actionable" data-vl-id:"cadreTab"
--------<Text-TabLabel> value:_t.label font-size:"14px" sk.fg:($activeTab == _t.tabKey ? "#eaf6ff" : "#7aa0c8") font-weight:"700" letter-spacing:"2px"
-----<Row-CadreBody> width:"100%" flex:"1" min-height:"0" gap:"6px" padding:"4px 0 0"
// Gender ratio
------<Col-CadreGender> width:"28%" gap:"4px" align-items:"center"
-------<Text-GenderH> value:"Gender Ratio" font-size:"13px" sk.fg:"#9fd4ff" letter-spacing:"1px"
-------<Col-GenderPieWrap> width:"100px" height:"100px" sk.radius:"50%" sk.bgImage:("conic-gradient(#25e8e0 0deg " + ($cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male").length > 0 ? $cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male")[0].value : 50) * 3.6 + "deg, #ff5aa8 " + ($cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male").length > 0 ? $cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male")[0].value : 50) * 3.6 + "deg 360deg)") align-items:"center" justify-content:"center"
-------<Row-GenderLeg> width:"100%" justify-content:"center" gap:"8px"
--------<For-GenderLegend> sourceArray:$cadreGenders.filter((_g) => _g.tabKey == $activeTab) loopVar:[_g,_gi] // VL-FIXED-LIST-OK: reason="fixed gender legend"
---------<Row-GLegRow> min-height:"16px" align-items:"center" gap:"4px"
----------<Col-GDot> width:"8px" height:"8px" sk.radius:"50%" sk.bg:_g.color
----------<Text-GLegL> value:(_g.label + " " + _g.value + "%") font-size:"11px" sk.fg:"#cfe6ff"
// Age distribution
------<Col-CadreAge> width:"38%" gap:"4px" padding:"0 4px"
-------<Text-AgeH> value:"Age Distribution" font-size:"13px" sk.fg:"#9fd4ff" letter-spacing:"1px" text-align:"center"
-------<For-CadreAges> sourceArray:$cadreAges.filter((_a) => _a.tabKey == $activeTab) loopVar:[_a,_ai] // VL-FIXED-LIST-OK: reason="fixed age bands"
--------<Col-AgeRow> width:"100%" flex:"1" min-height:"30px" gap:"3px"
---------<Row-AgeHead> width:"100%" justify-content:"space-between" align-items:"baseline"
----------<Text-AgeL> value:_a.label font-size:"11px" sk.fg:"#cfe6ff"
----------<Text-AgeV> value:_a.value font-size:"11px" sk.fg:_a.color font-family:"Consolas, monospace" font-weight:"700"
---------<Row-AgeBar> width:"100%" height:"8px" sk.bg:"rgba(80,180,255,0.10)" sk.borderColor:"rgba(80,180,255,0.20)" sk.borderWidth:"1px" overflow:"hidden"
----------<Col-AgeFill> width:(_a.pctNum + "%") height:"100%" sk.bg:_a.color
// Seniority
------<Col-CadreTitle> width:"34%" gap:"4px" align-items:"center"
-------<Text-TitleH> value:"Seniority" font-size:"13px" sk.fg:"#9fd4ff" letter-spacing:"1px"
-------<Col-TitleDonutWrap> width:"90px" height:"90px" sk.radius:"50%" sk.bgImage:"conic-gradient(#25e8e0 0deg 64deg, #ff5aa8 64deg 180deg, #ffd23a 180deg 306deg, #b06bff 306deg 360deg)" align-items:"center" justify-content:"center"
--------<Col-TitleHole> width:"42px" height:"42px" sk.radius:"50%" sk.bg:"#04122c"
-------<Col-TitleLegend> width:"100%" gap:"2px" padding:"2px"
--------<For-TitleLegend> sourceArray:$cadreTitles.filter((_tt) => _tt.tabKey == $activeTab) loopVar:[_tt,_tti] // VL-FIXED-LIST-OK: reason="fixed seniority legend"
---------<Row-TLegRow> width:"100%" min-height:"13px" align-items:"center" gap:"4px"
----------<Col-TLegDot> width:"6px" height:"6px" sk.radius:"50%" sk.bg:_tt.color
----------<Text-TLegLabel> value:_tt.label font-size:"10px" sk.fg:"#cfe6ff" flex:"1"
----------<Text-TLegVal> value:_tt.value font-size:"10px" sk.fg:_tt.color font-family:"Consolas, monospace" font-weight:"700"

// — Bottom 3 columns (flex 18) —
----<Row-BottomCols> width:"100%" flex:"1" min-height:"0" gap:"6px"
-----<Col-PanelOrg> width:"28%" height:"100%" min-height:"0" padding:"6px 10px 9px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"4px"
------<Row-TitleOrg> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
-------<Text-TOrg> value:"Help Desk" font-size:"14px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
------<Col-OrgKpis> width:"100%" flex:"1" min-height:"0" justify-content:"space-around" gap:"5px" padding:"4px"
-------<For-OrgKpis> sourceArray:$orgKpis loopVar:[_k,_ki] // VL-FIXED-LIST-OK: reason="2 fixed KPIs"
--------<Col-KpiBox> width:"100%" flex:"1" min-height:"0" align-items:"center" justify-content:"center" padding:"4px 4px" sk.bgImage:"linear-gradient(180deg, rgba(60,160,255,0.15), rgba(20,60,140,0.05))" sk.borderColor:"rgba(80,180,255,0.22)" sk.borderWidth:"1px"
---------<Text-KpiV> value:_k.value font-size:"32px" font-weight:"700" sk.fg:(_k.color == "yellow" ? "#ffd23a" : "#ff5aa8") font-family:"Consolas, monospace" line-height:"1"
---------<Text-KpiL> value:_k.label font-size:"13px" sk.fg:"#b9d8f5" letter-spacing:"1px" padding:"4px 0 0"
-----<Col-PanelFee> width:"32%" height:"100%" min-height:"0" padding:"6px 10px 9px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"4px"
------<Row-TitleFee> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
-------<Text-TFee> value:"Occupancy" font-size:"14px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
-------<Text-TFeeSub> value:"(%)" font-size:"11px" sk.fg:"#7aa0c8" padding:"0 0 0 4px"
------<Row-FeeBars> width:"100%" flex:"1" min-height:"0" align-items:"flex-end" justify-content:"space-around" padding:"4px 4px"
-------<For-Dues> sourceArray:$duesBars loopVar:[_d,_di] // VL-FIXED-LIST-OK: reason="5 fixed monthly bars"
--------<Col-FeeBarCol> width:"15%" align-items:"center" justify-content:"flex-end" gap:"3px" min-height:"0"
---------<Text-FeeVal> value:_d.value font-size:"10px" sk.fg:"#2bf08a" font-family:"Consolas, monospace"
---------<Col-FeeBar> width:"75%" height:((_d.value * 0.111) + "vh") sk.bgImage:"linear-gradient(180deg, #2bf08a 0%, rgba(43,240,138,0.30) 100%)" min-height:"6px"
---------<Text-FeeLabel> value:_d.monthLabel font-size:"10px" sk.fg:"#cfe6ff"
-----<Col-PanelSide> width:"38%" height:"100%" min-height:"0" padding:"6px 10px 9px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"4px"
------<Row-TitleSide> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
-------<Text-TSide> value:"Campus Events" font-size:"14px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
// Narrow-column layout: donut on top, full-width legend below, so legend text does not wrap at 1280
------<Col-SideBody> width:"100%" flex:"1" min-height:"0" gap:"4px" align-items:"center"
-------<Col-SideDonutWrap> width:"100%" align-items:"center" justify-content:"center"
--------<Col-SideDonut> width:"70px" height:"70px" sk.radius:"50%" sk.bgImage:"conic-gradient(#25e8e0 0deg 180deg, #ff5aa8 180deg 270deg, #2bf08a 270deg 342deg, #ffd23a 342deg 360deg)" align-items:"center" justify-content:"center"
---------<Col-SideHole> width:"40px" height:"40px" sk.radius:"50%" sk.bg:"#04122c" align-items:"center" justify-content:"center"
----------<Text-SideTotal> value:$platformMeta.sideJobTotal font-size:"14px" sk.fg:"#eaf6ff" font-weight:"700" font-family:"Consolas, monospace"
-------<Col-SideLegs> width:"100%" gap:"2px" padding:"0 2px"
--------<For-SideLeg> sourceArray:$sideJobSlices loopVar:[_sj,_sji] // VL-FIXED-LIST-OK: reason="4 event legend items"
---------<Row-SideLeg> width:"100%" min-height:"15px" align-items:"center" gap:"5px"
----------<Col-SideDot> width:"8px" height:"8px" sk.radius:"50%" sk.bg:_sj.color
----------<Text-SideL> value:_sj.label font-size:"10px" sk.fg:"#cfe6ff" flex:"1"
----------<Text-SideP> value:_sj.percent font-size:"10px" sk.fg:_sj.color font-family:"Consolas, monospace" font-weight:"700"

// ============ MIDDLE COLUMN (50%) — Engagement & Communications ============
---<Col-Mid> width:"50%" height:"100%" min-height:"0" gap:"8px"
----<Col-PanelStudy> width:"100%" flex:"1" min-height:"0" padding:"8px 14px 11px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"3px" overflow:"auto"
-----<Row-TitleStudy> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
------<Text-TStudy> value:"Engagement & Communications" font-size:"16px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
// Media coverage index
-----<Row-SubMedia> width:"100%" align-items:"center" gap:"6px" padding:"5px 4px 2px 12px" min-height:"22px"
------<Col-SubDot1> width:"8px" height:"8px" sk.bg:"#22e1ff"
------<Text-SubMedia> value:"Media Coverage Index" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
-----<Col-MediaRank> width:"100%" gap:"3px" padding:"2px 6px"
------<For-MediaRanks> sourceArray:$mediaRanks loopVar:[_m,_mi] // VL-FIXED-LIST-OK: reason="7 fixed media ranks"
-------<Row-MediaRankItem> width:"100%" min-height:"18px" align-items:"center" gap:"6px"
--------<Text-MediaIdx> value:(_mi + 1) width:"16px" sk.fg:"#7aa0c8" font-size:"10px" font-family:"Consolas, monospace"
--------<Text-MediaName> value:_m.label width:"34%" sk.fg:"#cfe6ff" font-size:"11px"
--------<Row-MediaBarOuter> flex:"1" height:"10px" sk.bg:"rgba(80,180,255,0.06)" overflow:"hidden"
---------<Col-MediaBarFill> width:(_m.barPct + "%") height:"100%" sk.bgImage:"linear-gradient(90deg, #0a8db0 0%, #22e1ff 100%)"
--------<Text-MediaVal> value:_m.value width:"42px" sk.fg:"#22e1ff" font-size:"11px" font-family:"Consolas, monospace" font-weight:"700" text-align:"right"
-----<Text-MediaNote> value:"*Composite score per unit, based on items published on the university news site, official social accounts, campus media and external outlets (as of Aug 24, 2022)" font-size:"9px" sk.fg:"#7aa0c8" line-height:"1.4" padding:"2px 6px"
// Social media reach
-----<Row-SubFusion> width:"100%" align-items:"center" gap:"6px" padding:"5px 4px 2px 12px" min-height:"22px"
------<Col-SubDot2> width:"8px" height:"8px" sk.bg:"#22e1ff"
------<Text-SubFusion> value:"Social Media Reach" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
-----<Col-MediaTableWrap> width:"100%" padding:"2px 6px"
------<Row-MediaHead> width:"100%" sk.bg:"rgba(80,180,255,0.06)" padding:"4px 4px" sk.borderBottom:"1px solid rgba(80,180,255,0.30)"
-------<Text-MHead1> value:"Official channels, 2022" width:"24%" font-size:"11px" sk.fg:"#7fc6ff" padding:"0 0 0 8px"
-------<For-MediaHead> sourceArray:$mediaTable loopVar:[_mt,_mti] // VL-FIXED-LIST-OK: reason="5 header columns"
--------<Text-MHeadCol> value:_mt.platform flex:"1" font-size:"11px" sk.fg:"#7fc6ff" text-align:"center"
------<Row-MediaPost> width:"100%" padding:"4px 4px" sk.borderBottom:"1px dashed rgba(80,180,255,0.15)"
-------<Text-MRowL1> value:"Posts" width:"24%" font-size:"11px" sk.fg:"#aac6e8" padding:"0 0 0 8px"
-------<For-MediaPost> sourceArray:$mediaTable loopVar:[_mt2,_mt2i] // VL-FIXED-LIST-OK: reason="5 post-count columns"
--------<Text-MPostV> value:_mt2.postCount flex:"1" font-size:"12px" sk.fg:"#d6ecff" font-family:"Consolas, monospace" text-align:"center"
------<Row-MediaRead> width:"100%" padding:"4px 4px"
-------<Text-MRowL2> value:"Total views" width:"24%" font-size:"11px" sk.fg:"#aac6e8" padding:"0 0 0 8px"
-------<For-MediaRead> sourceArray:$mediaTable loopVar:[_mt3,_mt3i] // VL-FIXED-LIST-OK: reason="5 view-count columns"
--------<Text-MReadV> value:_mt3.readCount flex:"1" font-size:"12px" sk.fg:"#ffd23a" font-family:"Consolas, monospace" font-weight:"700" text-align:"center"
// Training & workshops
-----<Row-SubStudyRow> width:"100%" justify-content:"space-between" align-items:"baseline" padding:"5px 4px 2px 12px" min-height:"22px"
------<Row-SubStudyL> align-items:"center" gap:"6px"
-------<Col-SubDot3> width:"8px" height:"8px" sk.bg:"#22e1ff"
-------<Text-SubStudy> value:"Training & Workshops" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
------<Row-StudyMeta> align-items:"center" gap:"8px"
-------<Text-StudyMeta1> value:"Courses published" font-size:"11px" sk.fg:"#a9c6e8"
-------<Col-StudyMetaBadge> padding:"1px 6px" sk.bg:"rgba(34,225,255,0.18)" sk.borderColor:"#22e1ff" sk.borderWidth:"1px"
--------<Text-StudyMeta2> value:"5" font-size:"11px" sk.fg:"#22e1ff" font-weight:"700"
-------<Text-StudyMeta3> value:"Sessions held" font-size:"11px" sk.fg:"#a9c6e8"
-------<Text-StudyMeta4> value:"102" font-size:"16px" sk.fg:"#22e1ff" font-weight:"700" font-family:"Consolas, monospace"
-------<Row-StudyLg1> align-items:"center" gap:"4px"
--------<Col-DotY> width:"9px" height:"9px" sk.radius:"50%" sk.bg:"#ffd23a"
--------<Text-StudyLg1> value:"Year" font-size:"11px" sk.fg:"#cfe6ff"
-------<Row-StudyLg2> align-items:"center" gap:"4px"
--------<Col-DotG> width:"9px" height:"9px" sk.radius:"50%" sk.bg:"#2bf08a"
--------<Text-StudyLg2> value:"Month" font-size:"11px" sk.fg:"#cfe6ff"
-----<Row-StudyBars> width:"100%" flex:"1" min-height:"0" align-items:"flex-end" justify-content:"space-around" padding:"5px 8px" gap:"6px"
------<For-StudyBars> sourceArray:$studyBars loopVar:[_sb,_sbi] // VL-FIXED-LIST-OK: reason="6 department paired bars"
-------<Col-StudyGroup> flex:"1" align-items:"center" justify-content:"flex-end" gap:"4px" min-height:"0"
--------<Row-StudyTwo> width:"100%" align-items:"flex-end" justify-content:"center" gap:"3px"
---------<Col-StudyAnnual> width:"42%" height:((_sb.annualVal * 1.0) + "vh") sk.bgImage:"linear-gradient(180deg, #ffd23a 0%, rgba(255,210,58,0.45) 100%)" min-height:"9px"
---------<Col-StudyMonthly> width:"42%" height:((_sb.monthlyVal * 1.0) + "vh") sk.bgImage:"linear-gradient(180deg, #2bf08a 0%, rgba(43,240,138,0.45) 100%)" min-height:"9px"
--------<Text-StudyGLabel> value:_sb.label font-size:"10px" sk.fg:"#a9c6e8" text-align:"center" line-height:"1.2"
// Satisfaction survey
-----<Row-SubOpinion> width:"100%" align-items:"center" gap:"6px" padding:"5px 4px 2px 12px" min-height:"22px"
------<Col-SubDot4> width:"8px" height:"8px" sk.bg:"#22e1ff"
------<Text-SubOpinion> value:"Satisfaction Survey" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
-----<Row-OpinionLeg> width:"100%" align-items:"center" gap:"18px" justify-content:"center" padding:"2px 6px"
------<Row-OpLeg1> align-items:"center" gap:"5px"
-------<Col-DotP> width:"11px" height:"11px" sk.radius:"50%" sk.bg:"#b06bff"
-------<Text-OpLeg1> value:"Students" font-size:"12px" sk.fg:"#cfe6ff"
------<Row-OpLeg2> align-items:"center" gap:"5px"
-------<Col-DotC> width:"11px" height:"11px" sk.radius:"50%" sk.bg:"#25e8e0"
-------<Text-OpLeg2> value:"Staff" font-size:"12px" sk.fg:"#cfe6ff"
-----<Row-OpinionBars> width:"100%" flex:"1" min-height:"0" align-items:"flex-end" justify-content:"space-around" padding:"3px 12px"
------<For-Opinions> sourceArray:$opinionAreas loopVar:[_op,_opi] // VL-FIXED-LIST-OK: reason="4 survey areas"
-------<Col-OpGroup> flex:"1" align-items:"center" justify-content:"flex-end" gap:"4px" min-height:"0"
--------<Row-OpTwo> width:"100%" align-items:"flex-end" justify-content:"center" gap:"4px"
---------<Col-OpPurple> width:"38%" height:((_op.partyVal * 0.111) + "vh") sk.bgImage:"linear-gradient(180deg, #b06bff 0%, rgba(176,107,255,0.30) 100%)" min-height:"6px"
---------<Col-OpCyan> width:"38%" height:((_op.disciplineVal * 0.111) + "vh") sk.bgImage:"linear-gradient(180deg, #25e8e0 0%, rgba(37,232,224,0.30) 100%)" min-height:"6px"
--------<Text-OpGLabel> value:_op.ageLabel font-size:"11px" sk.fg:"#a9c6e8"

// ============ RIGHT COLUMN (25%) — Facilities & Safety ============
---<Col-Right> width:"25%" height:"100%" min-height:"0" gap:"8px"
----<Col-PanelJijian> width:"100%" flex:"1" min-height:"0" padding:"8px 12px 11px" sk.bg:"rgba(8,28,72,0.55)" sk.borderColor:"rgba(80,180,255,0.30)" sk.borderWidth:"1px" gap:"3px" overflow:"auto"
-----<Row-TitleJijian> width:"100%" padding:"4px 8px 5px 14px" sk.bgImage:"linear-gradient(90deg, rgba(80,180,255,0.20) 0%, rgba(80,180,255,0.04) 60%, transparent 100%)" sk.borderLeft:"3px solid #22e1ff" align-items:"center"
------<Text-TJijian> value:"Facilities & Safety" font-size:"16px" sk.fg:"#eaf6ff" font-weight:"700" letter-spacing:"2px"
// Building Energy / Lab Safety blocks
-----<For-WarnGroups> sourceArray:$warningSummaries loopVar:[_w,_wi] // VL-FIXED-LIST-OK: reason="2 fixed alert groups"
------<Col-WarnBlock> width:"100%" flex:"1" min-height:"0" gap:"4px" padding:"4px 0"
-------<Row-WarnSubH> width:"100%" align-items:"center" gap:"6px" padding:"2px 4px 4px 12px" min-height:"22px"
--------<Col-WSubDot> width:"8px" height:"8px" sk.bg:"#22e1ff"
--------<Text-WarnSubH> value:_w.title font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
-------<Row-WarnHead> width:"100%" align-items:"center" gap:"8px" padding:"2px 6px"
--------<Row-WarnModel> align-items:"baseline" gap:"6px"
---------<Text-WModelL> value:"Alert rules" font-size:"12px" sk.fg:"#9fd4ff"
---------<Text-WModelV> value:_w.modelCount font-size:"24px" sk.fg:"#ffd23a" font-weight:"700" font-family:"Consolas, monospace"
--------<Col-WarnLegs> flex:"1" align-items:"flex-end" gap:"3px"
---------<Text-WTop> value:"Top 10 alerts" font-size:"10px" sk.fg:"#9fd4ff"
---------<Row-WarnPills> gap:"5px"
----------<Row-WPillBlue> padding:"2px 8px" sk.bgImage:"linear-gradient(135deg, #1ddc9a, #25e8e0)" sk.radius:"12px" align-items:"center" gap:"3px"
-----------<Text-WPB> value:_w.blueCount font-size:"11px" sk.fg:"#04244a" font-weight:"700" font-family:"Consolas, monospace"
-----------<Text-WPBL> value:"Low" font-size:"10px" sk.fg:"#04244a"
----------<Row-WPillYellow> padding:"2px 8px" sk.bgImage:"linear-gradient(135deg, #ffb429, #ffd23a)" sk.radius:"12px" align-items:"center" gap:"3px"
-----------<Text-WPY> value:_w.yellowCount font-size:"11px" sk.fg:"#3a2400" font-weight:"700" font-family:"Consolas, monospace"
-----------<Text-WPYL> value:"Medium" font-size:"10px" sk.fg:"#3a2400"
----------<Row-WPillRed> padding:"2px 8px" sk.bgImage:"linear-gradient(135deg, #ff3b6c, #ff7a8b)" sk.radius:"12px" align-items:"center" gap:"3px"
-----------<Text-WPR> value:_w.redCount font-size:"11px" sk.fg:"#fff" font-weight:"700" font-family:"Consolas, monospace"
-----------<Text-WPRL> value:"High" font-size:"10px" sk.fg:"#fff"
-------<Row-WarnBars> width:"100%" flex:"1" min-height:"0" align-items:"flex-end" justify-content:"space-around" padding:"4px 4px" gap:"3px"
--------<For-WBars> sourceArray:$warningBars.filter((_b) => _b.groupKey == _w.groupKey) loopVar:[_b,_bi] // VL-FIXED-LIST-OK: reason="Top 10 alert bars"
---------<Col-WBarGroup> flex:"1" align-items:"center" justify-content:"flex-end" gap:"2px" min-height:"0"
----------<Text-WBarV> value:_b.value font-size:"10px" sk.fg:_b.color font-family:"Consolas, monospace"
----------<Col-WBar> width:"75%" height:((_b.value * 0.18) + "vh") sk.bgImage:("linear-gradient(180deg, " + _b.color + " 0%, " + _b.color + "33 100%)") min-height:"10px"
----------<Text-WBarL> value:_b.modelLabel font-size:"9px" sk.fg:"#7aa0c8"
// Maintenance work orders
-----<Col-MajorBlock> width:"100%" gap:"4px" padding:"8px 4px 4px" sk.borderTop:"1px solid rgba(80,180,255,0.18)"
------<Row-MajorSubH> width:"100%" align-items:"center" gap:"6px" padding:"2px 4px 4px 12px" min-height:"22px"
-------<Col-MSubDot> width:"8px" height:"8px" sk.bg:"#22e1ff"
-------<Text-MajorSubH> value:"Maintenance Work Orders" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
------<Row-MajorHead> width:"100%" align-items:"center" justify-content:"space-between" padding:"0 4px"
-------<Row-MHL> align-items:"center" gap:"4px"
--------<Icon-Caret2> value:"f0da" fontSet:"fa-solid-900" font-size:"11px" sk.fg:"#22e1ff"
--------<Text-MHLabel> value:"Work orders (total)" font-size:"13px" sk.fg:"#9fd4ff" letter-spacing:"1px"
-------<Text-MHV> value:$majorEvent.totalCount font-size:"30px" sk.fg:"#ffd23a" font-weight:"700" font-family:"Consolas, monospace"
------<Row-MajorRow> width:"100%" align-items:"baseline" justify-content:"space-between" padding:"0 4px"
-------<Text-MajorDone> value:$majorEvent.doneCount font-size:"16px" sk.fg:"#d8ecff" font-family:"Consolas, monospace"
-------<Text-MajorPct> value:$majorEvent.pctLabel font-size:"18px" sk.fg:"#22e1ff" font-weight:"700" font-family:"Consolas, monospace"
------<Row-MajorBar> width:"100%" height:"11px" sk.bg:"rgba(80,180,255,0.10)" sk.borderColor:"rgba(80,180,255,0.25)" sk.borderWidth:"1px" overflow:"hidden"
-------<Col-MajorFill> width:($majorEvent.pctNum + "%") height:"100%" sk.bgImage:"linear-gradient(90deg, #0a8db0, #22e1ff)"

# Frontend Event Handlers
<Section-Dashboard "root">.@init()
-init()

<Col-TabBtn "cadreTab">.@click()
-$activeTab = _t.tabKey

# Frontend Internal Methods
METHOD init();RETURN {success:BOOL}
-<ServiceDomain-Dashboard "dashboardSvc">.GetDashboardData() -> _r
-IF !_r.success
--<SysUI>.showToast("Failed to load: " + _r.message,"error","",2)
--RETURN {success:false}
-$orgStats = _r.orgStats
-$memberDonut = _r.memberDonut
-$collegeRatios = _r.collegeRatios
-$incubationProjects = _r.incubationProjects
-$cadreTabs = _r.cadreTabs
-$cadreGenders = _r.cadreGenders
-$cadreAges = _r.cadreAges
-$cadreTitles = _r.cadreTitles
-$orgKpis = _r.orgKpis
-$duesBars = _r.duesBars
-$sideJobSlices = _r.sideJobSlices
-$mediaRanks = _r.mediaRanks
-$mediaTable = _r.mediaTable
-$studyBars = _r.studyBars
-$opinionAreas = _r.opinionAreas
-$warningSummaries = _r.warningSummaries
-$warningBars = _r.warningBars
-$majorEvent = _r.majorEvent
-$platformMeta = _r.platformMeta
-$loaded = true
-RETURN {success:true}

# Frontend Pipeline Funcs
</Section-Dashboard>
