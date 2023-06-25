be=20230617
en=20230623

python3      main.py     $be      $en     0-1     @TokinoSora            >  $be-$en/0-1_@TokinoSora/.log         &
python3      main.py     $be      $en     0-2     @Robocosan             >  $be-$en/0-2_@Robocosan/.log          &
python3      main.py     $be      $en     0-3     @AZKi                  >  $be-$en/0-3_@AZKi/.log               &
python3      main.py     $be      $en     0-4     @SakuraMiko            >  $be-$en/0-4_@SakuraMiko/.log         &
python3      main.py     $be      $en     0-5     @HoshimachiSuisei      >  $be-$en/0-5_@HoshimachiSuisei/.log   &
python3      main.py     $be      $en     1-6     @YozoraMel             >  $be-$en/1-6_@YozoraMel/.log          &
python3      main.py     $be      $en     1-7     @AkiRosenthal          >  $be-$en/1-7_@AkiRosenthal/.log       &
python3      main.py     $be      $en     1-8     @AkaiHaato             >  $be-$en/1-8_@AkaiHaato/.log          &
python3      main.py     $be      $en     1-9     @ShirakamiFubuki       >  $be-$en/1-9_@ShirakamiFubuki/.log    &
python3      main.py     $be      $en     1-10    @NatsuiroMatsuri       >  $be-$en/1-10_@NatsuiroMatsuri/.log   &
python3      main.py     $be      $en     2-11    @MinatoAqua            >  $be-$en/2-11_@MinatoAqua/.log        &
python3      main.py     $be      $en     2-12    @MurasakiShion         >  $be-$en/2-12_@MurasakiShion/.log     &
python3      main.py     $be      $en     2-13    @NakiriAyame           >  $be-$en/2-13_@NakiriAyame/.log       &
python3      main.py     $be      $en     2-14    @YuzukiChoco           >  $be-$en/2-14_@YuzukiChoco/.log       &
python3      main.py     $be      $en     2-15    @OozoraSubaru          >  $be-$en/2-15_@OozoraSubaru/.log      &
python3      main.py     $be      $en     3-16    @usadapekora           >  $be-$en/3-16_@usadapekora/.log       &
python3      main.py     $be      $en     3-17    @ShiranuiFlare         >  $be-$en/3-17_@ShiranuiFlare/.log     &
python3      main.py     $be      $en     3-18    @ShiroganeNoel         >  $be-$en/3-18_@ShiroganeNoel/.log     &
python3      main.py     $be      $en     3-19    @HoushouMarine         >  $be-$en/3-19_@HoushouMarine/.log     &
python3      main.py     $be      $en     4-20    @AmaneKanata           >  $be-$en/4-20_@AmaneKanata/.log       &
python3      main.py     $be      $en     4-21    @TsunomakiWatame       >  $be-$en/4-21_@TsunomakiWatame/.log   &
python3      main.py     $be      $en     4-22    @TokoyamiTowa          >  $be-$en/4-22_@TokoyamiTowa/.log      &
python3      main.py     $be      $en     4-23    @HimemoriLuna          >  $be-$en/4-23_@HimemoriLuna/.log      &
python3      main.py     $be      $en     5-24    @YukihanaLamy          >  $be-$en/5-24_@YukihanaLamy/.log      &
python3      main.py     $be      $en     5-25    @MomosuzuNene          >  $be-$en/5-25_@MomosuzuNene/.log      &
python3      main.py     $be      $en     5-26    @ShishiroBotan         >  $be-$en/5-26_@ShishiroBotan/.log     &
python3      main.py     $be      $en     5-27    @OmaruPolka            >  $be-$en/5-27_@OmaruPolka/.log        &
python3      main.py     $be      $en     6-28    @LaplusDarknesss       >  $be-$en/6-28_@LaplusDarknesss/.log   &
python3      main.py     $be      $en     6-29    @TakaneLui             >  $be-$en/6-29_@TakaneLui/.log         &
python3      main.py     $be      $en     6-30    @HakuiKoyori           >  $be-$en/6-30_@HakuiKoyori/.log       &
python3      main.py     $be      $en     6-31    @SakamataChloe         >  $be-$en/6-31_@SakamataChloe/.log     &
python3      main.py     $be      $en     6-32    @kazamairoha           >  $be-$en/6-32_@kazamairoha/.log       &
python3      main.py     $be      $en     G-33    @OokamiMio             >  $be-$en/G-33_@OokamiMio/.log         &
python3      main.py     $be      $en     G-34    @NekomataOkayu         >  $be-$en/G-34_@NekomataOkayu/.log     &
python3      main.py     $be      $en     G-35    @InugamiKorone         >  $be-$en/G-35_@InugamiKorone/.log     &


dirname=$be-$en
echo "ls $dirname/*/*_speed_RANK.tsv > $dirname/RANK_list.tsv" > ana.sh
echo "python3  analysis_RANK.py  20230617-20230623/RANK_list.tsv" >> ana.sh
