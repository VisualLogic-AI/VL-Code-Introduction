// VL_VERSION:4.3.0
// Preview: width:390px height:844px
<Section-DashboardMobile "root">

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

<Col-PageShellMobile> width:"100%" min-height:"100vh" overflow:"auto" sk.bg:"#04122c" sk.bgImage:"radial-gradient(circle at 50% 0%, rgba(8,40,90,0.6) 0%, rgba(4,18,44,1) 60%)" font-family:"-apple-system, BlinkMacSystemFont, Microsoft YaHei, sans-serif"
-<Col-MobileBody> width:"100%" padding:"12px 12px 24px" gap:"12px"

// ========== HEADER ==========
--<Col-MobileHeader> width:"100%" padding:"8px 0" gap:"6px" sk.borderBottom:"1px solid rgba(34,225,255,0.18)" align-items:"center"
---<Row-MBrand> width:"100%" align-items:"center" justify-content:"center" gap:"10px"
----<Col-MBadge> width:"34px" height:"34px" sk.bg:"#0a2a55" sk.radius:"50%" sk.borderColor:"#22e1ff" sk.borderWidth:"1px" align-items:"center" justify-content:"center"
-----<Text-MUniv> value:"UNIV" font-size:"9px" sk.fg:"#eaffff" font-weight:"700"
----<Col-MName> gap:"2px" align-items:"center"
-----<Text-MNameCn> value:$platformMeta.schoolCn font-size:"14px" sk.fg:"#eaffff" font-weight:"700" letter-spacing:"3px"
-----<Text-MNameEn> value:$platformMeta.schoolEn font-size:"9px" sk.fg:"rgba(234,255,255,0.65)" letter-spacing:"1px"
---<Text-MPlatformTitle> value:$platformMeta.title font-size:"20px" font-weight:"900" sk.fg:"#eaffff" letter-spacing:"4px" font-family:"Microsoft YaHei, sans-serif" text-align:"center"
---<Row-MMeta> width:"100%" justify-content:"center" gap:"10px" align-items:"baseline"
----<Text-MTime> value:"20:08:58" font-size:"14px" sk.fg:"#22e1ff" font-weight:"700" font-family:"Consolas, monospace"
----<Text-MDate> value:"2022/8/24" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"

// ========== Module 1: Campus Population ==========
--<Col-MPanelDangyuan> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"10px"
---<Row-MTitleDangyuan> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTDangyuan> value:"Campus Population" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Row-MOrgStats> width:"100%" justify-content:"space-around"
----<For-MOrgStats> sourceArray:$orgStats loopVar:[_s,_si] // VL-FIXED-LIST-OK: reason="3 fixed KPIs"
-----<Col-MStatBox> align-items:"center" gap:"2px" padding:"6px 8px" min-height:"60px"
------<Text-MStatV> value:_s.value font-size:"24px" font-weight:"900" sk.fg:"#22e1ff" font-family:"Consolas, monospace"
------<Text-MStatL> value:_s.label font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
---<Col-MDonutRow> width:"100%" align-items:"center" gap:"8px"
----<Col-MDonutPie> width:"110px" height:"110px" sk.radius:"50%" sk.bgImage:"conic-gradient(#25e8e0 0deg 245deg, #ff5aa8 245deg 320deg, #ffd23a 320deg 343deg, #b06bff 343deg 360deg)" align-items:"center" justify-content:"center"
-----<Col-MDonutHole> width:"64px" height:"64px" sk.radius:"50%" sk.bg:"#04122c" align-items:"center" justify-content:"center"
------<Text-MDonutTotal> value:"9446" font-size:"15px" sk.fg:"#eaffff" font-weight:"700" font-family:"Consolas, monospace"
----<Col-MDonutLegend> width:"100%" gap:"4px"
-----<For-MMemberLegend> sourceArray:$memberDonut loopVar:[_md,_mdi] // VL-FIXED-LIST-OK: reason="4 fixed donut legend items"
------<Row-MMemberRow> width:"100%" min-height:"18px" align-items:"center" gap:"6px"
-------<Col-MMemberDot> width:"8px" height:"8px" sk.radius:"50%" sk.bg:_md.color
-------<Text-MMemberL> value:_md.label font-size:"12px" sk.fg:"rgba(234,255,255,0.85)" flex:"1"
-------<Text-MMemberV> value:_md.value font-size:"12px" sk.fg:_md.color font-family:"Consolas, monospace" font-weight:"700"
---<Col-MCollegeRatios> width:"100%" gap:"8px"
----<For-MCollegeRatios> sourceArray:$collegeRatios loopVar:[_c,_ci] // VL-FIXED-LIST-OK: reason="2 fixed attendance ratios"
-----<Col-MCollegeRow> width:"100%" min-height:"44px" gap:"3px"
------<Row-MCollegeH> align-items:"center" gap:"6px"
-------<Icon-MCaret> value:"f0da" fontSet:"fa-solid-900" font-size:"11px" sk.fg:"#22e1ff"
-------<Text-MCollegeName> value:_c.label font-size:"13px" sk.fg:"#eaffff"
------<Row-MCollegeVals> width:"100%" justify-content:"space-between"
-------<Text-MCollegeFrac> value:(_c.currentVal + " / " + _c.totalVal) font-size:"11px" sk.fg:"rgba(234,255,255,0.6)" font-family:"Consolas, monospace"
-------<Text-MCollegePct> value:_c.pctLabel font-size:"13px" font-weight:"700" sk.fg:(_c.color == "green" ? "#2bf08a" : "#22e1ff") font-family:"Consolas, monospace"
------<Row-MCollegeBar> width:"100%" height:"6px" sk.bg:"rgba(255,255,255,0.08)" sk.radius:"2px" overflow:"hidden"
-------<Col-MCollegeFill> width:(_c.pctNum + "%") height:"100%" sk.radius:"2px" sk.bg:(_c.color == "green" ? "#2bf08a" : "#22e1ff")

// ========== Module 2: Campus Sites ==========
--<Col-MPanelMap> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"8px"
---<Row-MTitleMap> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTMap> value:"Campus Sites" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Col-MMapArea> width:"100%" min-height:"120px" sk.bg:"rgba(8,40,100,0.40)" sk.bgImage:"radial-gradient(circle at 50% 50%, rgba(34,225,255,0.18) 0%, rgba(8,40,100,0.4) 70%)" sk.borderColor:"rgba(34,225,255,0.25)" sk.borderWidth:"1px" align-items:"center" justify-content:"center" gap:"8px"
----<Text-MMapHint1> value:"Main Campus" font-size:"16px" sk.fg:"#22e1ff" font-weight:"700" letter-spacing:"4px"
----<Text-MMapHint2> value:"Overview of campus and partner sites" font-size:"11px" sk.fg:"rgba(234,255,255,0.55)"

// ========== Module 3: Key Projects ==========
--<Col-MPanelProjects> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"8px"
---<Row-MTitleProj> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTProj> value:"Key Projects" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Col-MProjList> width:"100%" gap:"8px"
----<For-MProjects> sourceArray:$incubationProjects loopVar:[_p,_pi] // VL-FIXED-LIST-OK: reason="5 fixed projects"
-----<Row-MProjItem> width:"100%" align-items:"center" gap:"8px" min-height:"28px"
------<Col-MProjTag> padding:"3px 10px" sk.bg:(_p.level == "State" ? "#ff5aa8" : "#22e1ff") sk.radius:"3px" align-items:"center" justify-content:"center" min-width:"44px"
-------<Text-MTagL> value:_p.level font-size:"11px" sk.fg:"#04122c" font-weight:"700"
------<Text-MProjTitle> value:_p.title font-size:"12px" sk.fg:"rgba(234,255,255,0.85)" line-height:"1.4" flex:"1"

// ========== Module 4-6: Workforce Tabs ==========
--<Col-MPanelCadre> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"10px"
---<Row-MTitleCadre> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTCadre> value:"Workforce Overview" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Row-MCadreTabs> width:"100%" align-items:"center" justify-content:"space-around" gap:"6px"
----<For-MCadreTabs> sourceArray:$cadreTabs loopVar:[_t,_ti] // VL-FIXED-LIST-OK: reason="3 fixed tab chips"
-----<Col-MTabBtn "cadreTab"> padding:"6px 12px" min-height:"32px" sk.bg:($activeTab == _t.tabKey ? "#22e1ff" : "rgba(34,225,255,0.10)") sk.radius:"4px" sk.borderColor:($activeTab == _t.tabKey ? "#22e1ff" : "rgba(34,225,255,0.30)") sk.borderWidth:"1px" align-items:"center" justify-content:"center" flex:"1" style:"actionable" data-vl-id:"cadreTab"
------<Text-MTabLabel> value:_t.label font-size:"12px" sk.fg:($activeTab == _t.tabKey ? "#04122c" : "#eaffff") font-weight:"700"
// — Gender + seniority (two donuts in one row)
---<Row-MGenderTitleRow> width:"100%" gap:"8px"
----<Col-MGenderBox> flex:"1" gap:"6px" align-items:"center" padding:"6px 0" sk.bg:"rgba(8,28,72,0.20)" sk.radius:"4px"
-----<Text-MGenderH> value:"Gender Ratio" font-size:"12px" sk.fg:"rgba(234,255,255,0.65)"
-----<Col-MGenderPieWrap> width:"86px" height:"86px" sk.radius:"50%" sk.bgImage:("conic-gradient(#25e8e0 0deg " + ($cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male").length > 0 ? $cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male")[0].value : 50) * 3.6 + "deg, #ff5aa8 " + ($cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male").length > 0 ? $cadreGenders.filter((_g) => _g.tabKey == $activeTab && _g.label == "Male")[0].value : 50) * 3.6 + "deg 360deg)") align-items:"center" justify-content:"center"
-----<Row-MGenderLeg> width:"100%" justify-content:"center" gap:"10px"
------<For-MGenderLegend> sourceArray:$cadreGenders.filter((_g) => _g.tabKey == $activeTab) loopVar:[_g,_gi] // VL-FIXED-LIST-OK: reason="2 fixed gender legend items"
-------<Row-MGLegRow> min-height:"18px" align-items:"center" gap:"4px"
--------<Col-MGDot> width:"7px" height:"7px" sk.radius:"50%" sk.bg:_g.color
--------<Text-MGLegL> value:(_g.label + " " + _g.value + "%") font-size:"10px" sk.fg:"rgba(234,255,255,0.75)"
----<Col-MTitleBox> flex:"1" gap:"6px" align-items:"center" padding:"6px 0" sk.bg:"rgba(8,28,72,0.20)" sk.radius:"4px"
-----<Text-MTitleH> value:"Seniority" font-size:"12px" sk.fg:"rgba(234,255,255,0.65)"
-----<Col-MTitleDonutWrap> width:"78px" height:"78px" sk.radius:"50%" sk.bgImage:"conic-gradient(#25e8e0 0deg 64deg, #ff5aa8 64deg 180deg, #ffd23a 180deg 306deg, #b06bff 306deg 360deg)" align-items:"center" justify-content:"center"
------<Col-MTitleHole> width:"40px" height:"40px" sk.radius:"50%" sk.bg:"#04122c"
-----<Col-MTitleLegend> width:"100%" gap:"3px" padding:"3px 6px"
------<For-MTitleLegend> sourceArray:$cadreTitles.filter((_tt) => _tt.tabKey == $activeTab) loopVar:[_tt,_tti] // VL-FIXED-LIST-OK: reason="4 fixed seniority legend items"
-------<Row-MTLegRow> width:"100%" min-height:"15px" align-items:"center" gap:"4px"
--------<Col-MTLegDot> width:"6px" height:"6px" sk.radius:"50%" sk.bg:_tt.color
--------<Text-MTLegLabel> value:_tt.label font-size:"10px" sk.fg:"rgba(234,255,255,0.75)" flex:"1"
--------<Text-MTLegVal> value:_tt.value font-size:"10px" sk.fg:_tt.color font-family:"Consolas, monospace"
// — Age distribution (standalone horizontal bar list)
---<Col-MAgeBox> width:"100%" gap:"6px" padding:"4px 4px"
----<Text-MAgeH> value:"Age Distribution" font-size:"12px" sk.fg:"rgba(234,255,255,0.65)"
----<For-MCadreAges> sourceArray:$cadreAges.filter((_a) => _a.tabKey == $activeTab) loopVar:[_a,_ai] // VL-FIXED-LIST-OK: reason="4 fixed age bands"
-----<Col-MAgeRow> width:"100%" min-height:"30px" gap:"3px"
------<Row-MAgeHead> width:"100%" justify-content:"space-between"
-------<Text-MAgeL> value:_a.label font-size:"11px" sk.fg:"rgba(234,255,255,0.75)"
-------<Text-MAgeV> value:_a.value font-size:"11px" sk.fg:_a.color font-family:"Consolas, monospace" font-weight:"700"
------<Row-MAgeBar> width:"100%" height:"8px" sk.bg:"rgba(255,255,255,0.08)" sk.radius:"3px" overflow:"hidden"
-------<Col-MAgeFill> width:(_a.pctNum + "%") height:"100%" sk.radius:"3px" sk.bg:_a.color

// ========== Module 7: Help Desk KPIs ==========
--<Col-MPanelOrg> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"8px"
---<Row-MTitleOrg> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTOrg> value:"Help Desk" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Row-MOrgKpis> width:"100%" justify-content:"space-around" align-items:"center" gap:"10px" padding:"6px 0"
----<For-MOrgKpis> sourceArray:$orgKpis loopVar:[_k,_ki] // VL-FIXED-LIST-OK: reason="2 fixed KPIs"
-----<Col-MKpiBox> min-height:"70px" align-items:"center" gap:"4px"
------<Text-MKpiV> value:_k.value font-size:"28px" font-weight:"900" sk.fg:(_k.color == "yellow" ? "#ffd23a" : "#ff5aa8") font-family:"Consolas, monospace"
------<Text-MKpiL> value:_k.label font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"

// ========== Module 8: Occupancy Bar Chart ==========
--<Col-MPanelFee> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"8px"
---<Row-MTitleFee> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTFee> value:"Occupancy (%)" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Row-MFeeBars> width:"100%" min-height:"110px" align-items:"flex-end" justify-content:"space-around" padding:"6px 8px" gap:"6px"
----<For-MDues> sourceArray:$duesBars loopVar:[_d,_di] // VL-FIXED-LIST-OK: reason="5 fixed monthly bars"
-----<Col-MFeeBarCol> width:"16%" align-items:"center" gap:"4px" min-height:"100px"
------<Text-MFeeVal> value:_d.value font-size:"11px" sk.fg:"#2bf08a" font-family:"Consolas, monospace"
------<Col-MFeeBar> width:"70%" height:(_d.value * 0.7 + "px") sk.bg:"#2bf08a" sk.bgImage:"linear-gradient(180deg, #2bf08a 0%, rgba(43,240,138,0.45) 100%)" sk.radius:"3px" min-height:"6px"
------<Text-MFeeLabel> value:_d.monthLabel font-size:"10px" sk.fg:"rgba(234,255,255,0.7)"

// ========== Module 9: Campus Events ==========
--<Col-MPanelSide> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"10px"
---<Row-MTitleSide> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTSide> value:"Campus Events" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Row-MSideBody> width:"100%" gap:"10px" align-items:"center"
----<Col-MSideDonutWrap> width:"110px" align-items:"center" justify-content:"center"
-----<Col-MSideDonut> width:"96px" height:"96px" sk.radius:"50%" sk.bgImage:"conic-gradient(#25e8e0 0deg 180deg, #ff5aa8 180deg 270deg, #2bf08a 270deg 342deg, #ffd23a 342deg 360deg)" align-items:"center" justify-content:"center"
------<Col-MSideHole> width:"54px" height:"54px" sk.radius:"50%" sk.bg:"#04122c" align-items:"center" justify-content:"center"
-------<Text-MSideTotal> value:$platformMeta.sideJobTotal font-size:"17px" sk.fg:"#eaffff" font-weight:"900" font-family:"Consolas, monospace"
----<Col-MSideLegs> flex:"1" gap:"6px"
-----<For-MSideLeg> sourceArray:$sideJobSlices loopVar:[_sj,_sji] // VL-FIXED-LIST-OK: reason="4 fixed event slices"
------<Row-MSideLeg> width:"100%" min-height:"20px" align-items:"center" gap:"6px"
-------<Col-MSideDot> width:"8px" height:"8px" sk.radius:"50%" sk.bg:_sj.color
-------<Text-MSideL> value:_sj.label font-size:"11px" sk.fg:"rgba(234,255,255,0.85)" flex:"1"
-------<Text-MSideP> value:_sj.percent font-size:"11px" sk.fg:_sj.color font-family:"Consolas, monospace" font-weight:"700"

// ========== Module 10: Engagement & Communications ==========
--<Col-MPanelStudy> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"10px"
---<Row-MTitleStudy> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTStudy> value:"Engagement & Communications" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
// Media coverage index
---<Row-MSubMediaWrap> width:"100%" align-items:"center" gap:"6px"
----<Col-MSubDot1> width:"7px" height:"7px" sk.bg:"#22e1ff"
----<Text-MSubMedia> value:"Media Coverage Index" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
---<Col-MMediaRank> width:"100%" gap:"6px"
----<For-MMediaRanks> sourceArray:$mediaRanks loopVar:[_m,_mi] // VL-FIXED-LIST-OK: reason="7 fixed media ranks"
-----<Row-MMediaRankItem> width:"100%" min-height:"28px" align-items:"center" gap:"6px"
------<Text-MMediaIdx> value:(_mi + 1) width:"18px" sk.fg:"rgba(234,255,255,0.55)" font-size:"11px" font-family:"Consolas, monospace"
------<Text-MMediaName> value:_m.label flex:"1" sk.fg:"rgba(234,255,255,0.85)" font-size:"11px" line-height:"1.4"
------<Text-MMediaVal> value:_m.value width:"48px" sk.fg:"#22e1ff" font-size:"12px" font-family:"Consolas, monospace" font-weight:"700"
---<Row-MMediaBarOuter> width:"100%" height:"4px" sk.bg:"rgba(255,255,255,0.04)"
// Social media reach: card layout
---<Row-MSubFusionWrap> width:"100%" align-items:"center" gap:"6px"
----<Col-MSubDot2> width:"7px" height:"7px" sk.bg:"#22e1ff"
----<Text-MSubFusion> value:"Social Media Reach" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
---<Col-MFusionList> width:"100%" gap:"6px"
----<For-MFusion> sourceArray:$mediaTable loopVar:[_mt,_mti] // VL-FIXED-LIST-OK: reason="5 fixed social platforms"
-----<Row-MFusionItem> width:"100%" min-height:"36px" align-items:"center" gap:"8px" padding:"4px 6px" sk.bg:"rgba(34,225,255,0.06)" sk.radius:"3px"
------<Text-MFusionPlatform> value:_mt.platform width:"22%" sk.fg:"#22e1ff" font-size:"12px" font-weight:"700"
------<Col-MFusionPost> flex:"1" align-items:"center"
-------<Text-MFusionPostL> value:"Posts" font-size:"9px" sk.fg:"rgba(234,255,255,0.55)"
-------<Text-MFusionPostV> value:_mt.postCount font-size:"13px" sk.fg:"#eaffff" font-family:"Consolas, monospace" font-weight:"700"
------<Col-MFusionRead> flex:"1" align-items:"center"
-------<Text-MFusionReadL> value:"Views" font-size:"9px" sk.fg:"rgba(234,255,255,0.55)"
-------<Text-MFusionReadV> value:_mt.readCount font-size:"13px" sk.fg:"#ffd23a" font-family:"Consolas, monospace" font-weight:"700"
// Training & workshops
---<Row-MSubStudyWrap> width:"100%" align-items:"center" gap:"6px"
----<Col-MSubDot3> width:"7px" height:"7px" sk.bg:"#22e1ff"
----<Text-MSubStudy> value:"Training & Workshops" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
---<Row-MStudyMeta> width:"100%" align-items:"baseline" gap:"6px" padding:"2px 0"
----<Text-MStudyMeta1> value:"Courses published" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
----<Text-MStudyMeta2> value:"5" font-size:"12px" sk.fg:"#ffd23a" font-weight:"700"
----<Text-MStudyMeta3> value:"Sessions held" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
----<Text-MStudyMeta4> value:"102" font-size:"14px" sk.fg:"#ffd23a" font-weight:"900"
---<Row-MStudyLegend> width:"100%" align-items:"center" gap:"12px"
----<Row-MStudyLg1> align-items:"center" gap:"4px"
-----<Col-MDotY> width:"7px" height:"7px" sk.radius:"50%" sk.bg:"#ffd23a"
-----<Text-MStudyLg1> value:"Year" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
----<Row-MStudyLg2> align-items:"center" gap:"4px"
-----<Col-MDotG> width:"7px" height:"7px" sk.radius:"50%" sk.bg:"#2bf08a"
-----<Text-MStudyLg2> value:"Month" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
---<Row-MStudyBars> width:"100%" min-height:"120px" align-items:"flex-end" justify-content:"space-around" padding:"6px 4px" gap:"4px"
----<For-MStudyBars> sourceArray:$studyBars loopVar:[_sb,_sbi] // VL-FIXED-LIST-OK: reason="6 fixed department paired bars"
-----<Col-MStudyGroup> flex:"1" align-items:"center" gap:"4px" min-height:"110px"
------<Row-MStudyTwo> width:"100%" align-items:"flex-end" justify-content:"center" gap:"2px" flex:"1" min-height:"0"
-------<Col-MStudyAnnual> width:"42%" height:(_sb.annualVal * 10 + "px") sk.bg:"#ffd23a" sk.bgImage:"linear-gradient(180deg, #ffd23a 0%, rgba(255,210,58,0.45) 100%)" sk.radius:"2px" min-height:"8px"
-------<Col-MStudyMonthly> width:"42%" height:(_sb.monthlyVal * 10 + "px") sk.bg:"#2bf08a" sk.bgImage:"linear-gradient(180deg, #2bf08a 0%, rgba(43,240,138,0.45) 100%)" sk.radius:"2px" min-height:"8px"
------<Text-MStudyGLabel> value:_sb.label font-size:"9px" sk.fg:"rgba(234,255,255,0.65)" text-align:"center" line-height:"1.2"
// Satisfaction survey
---<Row-MSubOpinionWrap> width:"100%" align-items:"center" gap:"6px"
----<Col-MSubDot4> width:"7px" height:"7px" sk.bg:"#22e1ff"
----<Text-MSubOpinion> value:"Satisfaction Survey" font-size:"14px" sk.fg:"#cfe6ff" letter-spacing:"1px"
---<Row-MOpinionLeg> width:"100%" align-items:"center" gap:"12px"
----<Row-MOpLeg1> align-items:"center" gap:"4px"
-----<Col-MDotP> width:"7px" height:"7px" sk.radius:"50%" sk.bg:"#b06bff"
-----<Text-MOpLeg1> value:"Students" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
----<Row-MOpLeg2> align-items:"center" gap:"4px"
-----<Col-MDotC> width:"7px" height:"7px" sk.radius:"50%" sk.bg:"#25e8e0"
-----<Text-MOpLeg2> value:"Staff" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
---<Row-MOpinionBars> width:"100%" min-height:"100px" align-items:"flex-end" justify-content:"space-around" padding:"4px"
----<For-MOpinions> sourceArray:$opinionAreas loopVar:[_op,_opi] // VL-FIXED-LIST-OK: reason="4 fixed survey areas"
-----<Col-MOpGroup> flex:"1" align-items:"center" gap:"4px" min-height:"90px"
------<Row-MOpTwo> width:"100%" align-items:"flex-end" justify-content:"center" gap:"3px" flex:"1" min-height:"0"
-------<Col-MOpPurple> width:"38%" height:(_op.partyVal * 0.85 + "px") sk.bg:"#b06bff" sk.bgImage:"linear-gradient(180deg, #b06bff 0%, rgba(176,107,255,0.30) 100%)" sk.radius:"2px" min-height:"6px"
-------<Col-MOpCyan> width:"38%" height:(_op.disciplineVal * 0.85 + "px") sk.bg:"#25e8e0" sk.bgImage:"linear-gradient(180deg, #25e8e0 0%, rgba(37,232,224,0.30) 100%)" sk.radius:"2px" min-height:"6px"
------<Text-MOpGLabel> value:_op.ageLabel font-size:"10px" sk.fg:"rgba(234,255,255,0.65)"

// ========== Module 11-13: Facilities & Safety ==========
--<Col-MPanelJijian> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"10px"
---<Row-MTitleJijian> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTJijian> value:"Facilities & Safety" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<For-MWarnGroups> sourceArray:$warningSummaries loopVar:[_w,_wi] // VL-FIXED-LIST-OK: reason="2 fixed alert groups"
----<Col-MWarnBlock> width:"100%" min-height:"220px" gap:"8px" padding:"6px 0"
-----<Text-MWarnSubH> value:_w.title font-size:"14px" sk.fg:"#22e1ff" letter-spacing:"2px" font-weight:"700"
-----<Row-MWarnHead> width:"100%" align-items:"center" justify-content:"space-between" gap:"6px"
------<Row-MWarnModel> align-items:"baseline" gap:"6px"
-------<Text-MWModelL> value:"Alert rules" font-size:"11px" sk.fg:"rgba(234,255,255,0.7)"
-------<Text-MWModelV> value:_w.modelCount font-size:"26px" sk.fg:"#22e1ff" font-weight:"900" font-family:"Consolas, monospace"
------<Col-MWarnLegs> align-items:"flex-end" gap:"4px"
-------<Text-MWTop> value:"Top 10 alerts" font-size:"10px" sk.fg:"rgba(234,255,255,0.55)"
-------<Row-MWarnPills> gap:"4px"
--------<Row-MWPillBlue> padding:"3px 7px" sk.bg:"rgba(34,225,255,0.25)" sk.radius:"3px" align-items:"center" gap:"3px"
---------<Text-MWPB> value:_w.blueCount font-size:"11px" sk.fg:"#22e1ff" font-weight:"700" font-family:"Consolas, monospace"
---------<Text-MWPBL> value:"Low" font-size:"10px" sk.fg:"#22e1ff"
--------<Row-MWPillYellow> padding:"3px 7px" sk.bg:"rgba(255,210,58,0.20)" sk.radius:"3px" align-items:"center" gap:"3px"
---------<Text-MWPY> value:_w.yellowCount font-size:"11px" sk.fg:"#ffd23a" font-weight:"700" font-family:"Consolas, monospace"
---------<Text-MWPYL> value:"Med" font-size:"10px" sk.fg:"#ffd23a"
--------<Row-MWPillRed> padding:"3px 7px" sk.bg:"rgba(255,91,110,0.25)" sk.radius:"3px" align-items:"center" gap:"3px"
---------<Text-MWPR> value:_w.redCount font-size:"11px" sk.fg:"#ff5b6e" font-weight:"700" font-family:"Consolas, monospace"
---------<Text-MWPRL> value:"High" font-size:"10px" sk.fg:"#ff5b6e"
-----<Row-MWarnBars> width:"100%" min-height:"120px" align-items:"flex-end" justify-content:"space-around" padding:"4px 2px" gap:"3px"
------<For-MWBars> sourceArray:$warningBars.filter((_b) => _b.groupKey == _w.groupKey) loopVar:[_b,_bi] // VL-FIXED-LIST-OK: reason="Top 10 fixed alert bars"
-------<Col-MWBarGroup> flex:"1" align-items:"center" gap:"3px" min-height:"110px"
--------<Text-MWBarV> value:_b.value font-size:"10px" sk.fg:_b.color font-family:"Consolas, monospace"
--------<Col-MWBar> width:"75%" height:(_b.value * 1.05 + "px") sk.bg:_b.color sk.bgImage:("linear-gradient(180deg, " + _b.color + " 0%, " + _b.color + "33 100%)") sk.radius:"2px" min-height:"6px"
--------<Text-MWBarL> value:_b.modelLabel font-size:"8px" sk.fg:"rgba(234,255,255,0.55)"

// ========== Module 14: Maintenance Work Orders ==========
--<Col-MPanelMajor> width:"100%" padding:"10px 12px" sk.bg:"rgba(8,28,72,0.42)" sk.borderColor:"rgba(34,225,255,0.35)" sk.borderWidth:"1px" gap:"8px"
---<Row-MTitleMajor> width:"100%" padding:"4px 6px" sk.bgImage:"linear-gradient(90deg, rgba(34,225,255,0.25) 0%, transparent 70%)" sk.borderLeft:"3px solid #22e1ff"
----<Text-MTMajor> value:"Maintenance Work Orders" font-size:"15px" sk.fg:"#eaffff" font-weight:"700"
---<Row-MMajorHead> width:"100%" align-items:"center" justify-content:"space-between"
----<Row-MMHL> align-items:"center" gap:"6px"
-----<Icon-MCaret2> value:"f0da" fontSet:"fa-solid-900" font-size:"12px" sk.fg:"#22e1ff"
-----<Text-MMHLabel> value:"Work orders (total)" font-size:"13px" sk.fg:"rgba(234,255,255,0.85)"
----<Text-MMHV> value:$majorEvent.totalCount font-size:"30px" sk.fg:"#ffd23a" font-weight:"900" font-family:"Consolas, monospace"
---<Row-MMajorRow> width:"100%" align-items:"baseline" justify-content:"space-between"
----<Col-MMajorDoneBlock> gap:"2px"
-----<Text-MMajorDoneL> value:"Completed" font-size:"10px" sk.fg:"rgba(234,255,255,0.55)"
-----<Text-MMajorDone> value:$majorEvent.doneCount font-size:"22px" sk.fg:"#eaffff" font-weight:"700" font-family:"Consolas, monospace"
----<Text-MMajorPct> value:$majorEvent.pctLabel font-size:"24px" sk.fg:"#22e1ff" font-weight:"900" font-family:"Consolas, monospace"
---<Row-MMajorBar> width:"100%" height:"14px" sk.bg:"rgba(255,255,255,0.08)" sk.radius:"4px" overflow:"hidden"
----<Col-MMajorFill> width:($majorEvent.pctNum + "%") height:"100%" sk.bgImage:"linear-gradient(90deg, #22e1ff 0%, #25e8e0 100%)" sk.radius:"4px"

# Frontend Event Handlers
<Section-DashboardMobile "root">.@init()
-init()

<Col-MTabBtn "cadreTab">.@click()
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
</Section-DashboardMobile>
