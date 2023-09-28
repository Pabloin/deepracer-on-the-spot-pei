


class MyParams:
    
    waypoint  = lambda wp : MyParams.waypoints[wp]
    waypointX = lambda wp : MyParams.waypoints[wp][0]
    waypointY = lambda wp : MyParams.waypoints[wp][1]

    waypoints= [(4.858334541320801, -3.9953720569610596), (4.654623508453369, -4.217042446136475), (4.429752826690674, -4.417214512825012), (4.184256672859192, -4.59135890007019), (3.9298255443573, -4.752535581588745), (3.673319458961487, -4.9103920459747314), (3.415688991546631, -5.06640887260437), (3.157860040664673, -5.2220964431762695), (2.900552988052368, -5.378645896911621), (2.6422219276428223, -5.533502101898193), (2.383773446083069, -5.688159465789795), (2.1251325011253357, -5.8424952030181885), (1.8663389682769775, -5.996574878692627), (1.6074479818344116, -6.1504905223846436), (1.3485020399093628, -6.304313898086548), (1.089547485113144, -6.458123683929443), (0.8306315839290619, -6.61199688911438), (0.5717997997999191, -6.766013145446777), (0.3130980599671602, -6.920246601104736), (0.05458249896764755, -7.074792385101318), (-0.20374905690550804, -7.229645490646362), (-0.4616483598947525, -7.385216951370239), (-0.7200789600610733, -7.539885759353638), (-0.9959478676319122, -7.659351110458374), (-1.2923229932785034, -7.707080125808716), (-1.5907660126686096, -7.672801971435547), (-1.8743025064468384, -7.572548151016235), (-2.1408474445343018, -7.4324140548706055), (-2.4026089906692505, -7.283437013626099), (-2.664987564086914, -7.13555645942688), (-2.9277790784835815, -6.988399982452393), (-3.1906464099884033, -6.8413779735565186), (-3.4539270401000945, -6.695097446441652), (-3.7173709869384766, -6.5491108894348145), (-3.9810074567794844, -6.403472900390622), (-4.244800567626953, -6.2581188678741455), (-4.50872015953064, -6.112993955612183), (-4.772739887237553, -5.968051910400388), (-5.036830663681032, -5.823238611221313), (-5.300961494445801, -5.678500175476074), (-5.565105438232422, -5.533783912658691), (-5.829236030578613, -5.389043569564819), (-6.093324899673462, -5.244227409362793), (-6.357321500778198, -5.099242925643921), (-6.621283054351807, -4.95419454574585), (-6.885021924972534, -4.808742523193359), (-7.139628887176514, -4.648554086685181), (-7.361920595169067, -4.446040868759155), (-7.5183820724487305, -4.1911091804504395), (-7.5350682735443115, -3.8938859701156616), (-7.42689847946167, -3.6140815019607544), (-7.284416198730469, -3.348726987838745), (-7.143769025802612, -3.0823949575424194), (-7.00461220741272, -2.81528103351593), (-6.866581916809082, -2.5475831031799316), (-6.729351043701172, -2.2794744968414307), (-6.592571020126343, -2.0111350417137146), (-6.455732822418213, -1.7428255081176758), (-6.318326950073242, -1.474806010723114), (-6.179857969284058, -1.2073353230953217), (-6.041717529296875, -0.9397014677524567), (-5.9454615116119385, -0.6823945939540863), (-6.074353933334351, -0.36682317964732647), (-6.322118043899536, -0.2269417643547058), (-6.5847954750061035, -0.07959379255771637), (-6.8495423793792725, 0.06401430070400238), (-7.1148176193237305, 0.2066461443901062), (-7.379422903060913, 0.3505147360265255), (-7.642247676849365, 0.49760784208774567), (-7.902097702026367, 0.6498885080218315), (-8.157618999481201, 0.8093142360448837), (-8.40278959274292, 0.9841479957103729), (-8.627638339996338, 1.1843503713607788), (-8.820991516113281, 1.4149389863014221), (-8.967172622680664, 1.6777905225753784), (-9.050086498260498, 1.966804027557373), (-9.063097476959229, 2.2673009634017944), (-9.01515007019043, 2.564409017562866), (-8.922507286071777, 2.8507765531539917), (-8.799120426177979, 3.125439405441284), (-8.658244609832764, 3.3916244506835938), (-8.511792659759521, 3.6548060178756714), (-8.361048221588135, 3.9155534505844116), (-8.206440687179565, 4.174028992652893), (-8.048728466033936, 4.430624485015869), (-7.889913797378541, 4.686539649963377), (-7.730062007904054, 4.941807508468626), (-7.558359861373902, 5.188997030258177), (-7.331450939178467, 5.3842058181762695), (-7.040247201919556, 5.443227529525757), (-6.750200033187866, 5.366579055786133), (-6.478861570358276, 5.236021995544434), (-6.2094550132751465, 5.101376056671143), (-5.941605567932129, 4.963643312454224), (-5.674785614013672, 4.823923587799072), (-5.408709526062012, 4.682791471481323), (-5.143102645874023, 4.540778875350952), (-4.877570390701294, 4.39862859249115), (-4.611133813858032, 4.258177399635315), (-4.344216823577881, 4.118643403053284), (-4.077224016189575, 3.9792546033859253), (-3.8105589151382446, 3.839238405227661), (-3.544493079185486, 3.6980879306793213), (-3.278823971748352, 3.556191086769104), (-3.0133529901504517, 3.4139245748519897), (-2.747880458831787, 3.2716615200042725), (-2.4822059869766235, 3.12977397441864), (-2.2161329984664917, 2.988636612892151), (-1.9494659900665283, 2.8486239910125732), (-1.6820155382156372, 2.7101144790649414), (-1.4135979413986206, 2.5734879970550537), (-1.1440298855304718, 2.4391475319862366), (-0.8731828033924103, 2.3074000477790833), (-0.6006825119256969, 2.17911946773529), (-0.3285473473370075, 2.049994468688965), (-0.05966624617576599, 1.9143550395965576), (0.20552777871489525, 1.7715259790420532), (0.46984773874282837, 1.6271355152130127), (0.7366959452629089, 1.4874430298805237), (1.0110141932964325, 1.3630084693431854), (1.2983485460281372, 1.2728352844715118), (1.5981324911117554, 1.2489668130874634), (1.8899085521697998, 1.3210166990756989), (2.1465704441070557, 1.4786189794540405), (2.3643720149993896, 1.687063455581665), (2.552460551261902, 1.9226015210151672), (2.719522476196289, 2.1732495427131653), (2.8742510080337524, 2.4317370653152466), (3.0171974897384644, 2.696776032447815), (3.1182678937911987, 2.979817509651184), (3.169144034385681, 3.276620030403137), (3.218472480773926, 3.5737404823303223), (3.2536205053329468, 3.872851014137268), (3.2822024822235107, 4.172678470611572), (3.305191993713379, 4.4729859828948975), (3.3213889598846436, 4.773735046386719), (3.3282519578933716, 5.074843406677246), (3.319854497909546, 5.375889539718628), (3.27810001373291, 5.673871040344238), (3.27810001373291, 5.673871040344238), (3.1856003999710083, 5.9604339599609375), (3.086727499961853, 6.244928598403931), (3.0845890045166016, 6.5293869972229), (3.287795066833496, 6.751359462738037), (3.5160820484161377, 6.947789430618286), (3.754204034805298, 7.1322021484375), (3.998484969139099, 7.308374881744385), (4.248196005821228, 7.476767539978027), (4.511290073394775, 7.6220948696136475), (4.8033764362335205, 7.689007997512817), (5.103668451309204, 7.674888610839844), (5.401219606399536, 7.628126859664917), (5.696866989135742, 7.570626258850098), (5.990026950836182, 7.501545190811157), (6.280209064483643, 7.420871019363403), (6.566977500915527, 7.328797817230225), (6.850013494491577, 7.225820064544678), (7.129150152206421, 7.112696886062622), (7.404396057128906, 6.990411996841431), (7.675936937332153, 6.860105037689209), (7.944098234176636, 6.722976922988892), (8.209386110305786, 6.580363988876343), (8.472174167633057, 6.4332005977630615), (8.73464298248291, 6.285467147827148), (8.940507411956787, 6.077727556228638), (9.019631385803223, 5.787655353546143), (9.0577712059021, 5.48898458480835), (9.071599960327148, 5.1881797313690186), (9.020819664001465, 4.89298152923584), (8.898412704467773, 4.617997884750366), (8.764861583709717, 4.348037958145142), (8.63017463684082, 4.078641891479492), (8.495630741119385, 3.80917489528656), (8.362359762191772, 3.539076566696167), (8.231432914733887, 3.2678345441818237), (8.103992938995361, 2.9949405193328857), (7.990121841430664, 2.7166720628738403), (7.969041585922241, 2.416975498199463), (7.966020584106445, 2.115950584411621), (7.967590093612671, 1.8148269653320312), (7.950721263885498, 1.5146420001983643), (7.837175369262695, 1.2373765110969543), (7.692538022994995, 0.9731768369674683), (7.548962354660034, 0.7084121406078339), (7.404866933822632, 0.44392969459295273), (7.2603676319122314, 0.1796671412885189), (7.115480661392212, -0.08438265323638916), (6.970180034637451, -0.34820544347167015), (6.824462890625, -0.6117984354496002), (6.678318023681641, -0.8751546144485474), (6.5317370891571045, -1.1382680237293243), (6.384710073471069, -1.4011324644088745), (6.237231016159058, -1.663743495941162), (6.089274644851685, -1.9260855317115784), (5.9408910274505615, -2.188187003135681), (5.791924953460693, -2.4499579668045044), (5.642048358917236, -2.7112075090408325), (5.491778612136841, -2.9722315073013306), (5.341022968292236, -3.2329760789871216), (5.189697504043579, -3.4933894872665405), (5.036058664321899, -3.7524194717407227), (4.858334541320801, -3.9953720569610596)]



