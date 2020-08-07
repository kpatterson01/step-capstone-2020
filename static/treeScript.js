/*Created by Kayla Patterson on 07/23/2020
* Used D3.js to construct tree hierachy
*/

// Calcuate distance and usage similarity
async function calculate() {
  var employee_one_id = document.getElementById("user_2");
  var employee_two_id = document.getElementById("user_1");

  var data = {
    "employee_one_id": employee_one_id.value,
    "employee_two_id": employee_two_id.value
  }

  //Make requests to backend
  var distanceResponse = await fetch(`${window.origin}/api/distance`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })

  var usageResponse = await fetch(`${window.origin}/api/usage`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })

  var distanceData = await distanceResponse.json();
  var usageData = await usageResponse.json();
  console.log(distanceData);
  console.log(usageData);

  // Display metrics on sidebar
  if(distanceResponse.status == 200) {
    document.getElementById("distance").innerHTML = 'Distance: '+ distanceData.data;
  } else {
    document.getElementById("distance").innerHTML = 'Employee not found.';
  }

  if(usageResponse.status == 200) {
    document.getElementById("usage").innerHTML = 'Usage: '+ usageData.data + '%';
  } else {
    document.getElementById("usage").innerHTML = 'No resources found for one or more employee.';
  }
}

var treeData ={
  "name": 258004,
  "children": [
    {
      "name": 123765,
      "children": [
        {
          "name": 75573
        },
        {
          "name": 15316
        },
        {
          "name": 258111
        },
        {
          "name": 199515,
          "children": [
            {
              "name": 194521,
              "children": [
                {
                  "name": 162929
                },
                {
                  "name": 224709
                },
                {
                  "name": 265330
                }
              ]
            },
            {
              "name": 260201
            },
            {
              "name": 121974
            },
            {
              "name": 29844
            },
            {
              "name": 117440
            },
            {
              "name": 191354
            },
            {
              "name": 214037
            }
          ]
        },
        {
          "name": 232841
        },
        {
          "name": 158445
        }
      ]
    },
    {
      "name": 186284,
      "children": [
        {
          "name": 112981
        },
        {
          "name": 124200
        }
      ]
    },
    {
      "name": 262783,
      "children": [
        {
          "name": 210255,
          "children": [
            {
              "name": 179595,
              "children": [
                {
                  "name": 7880,
                  "children": [
                    {
                      "name": 2237
                    },
                    {
                      "name": 730
                    },
                    {
                      "name": 195496
                    }
                  ]
                },
                {
                  "name": 25825
                },
                {
                  "name": 50311
                },
                {
                  "name": 257874,
                  "children": [
                    {
                      "name": 52184
                    },
                    {
                      "name": 235288
                    },
                    {
                      "name": 10960
                    },
                    {
                      "name": 211588
                    },
                    {
                      "name": 64541
                    }
                  ]
                },
                {
                  "name": 139485
                },
                {
                  "name": 82096
                }
              ]
            },
            {
              "name": 60114,
              "children": [
                {
                  "name": 207811
                },
                {
                  "name": 24066
                },
                {
                  "name": 89312,
                  "children": [
                    {
                      "name": 8000
                    },
                    {
                      "name": 35055
                    },
                    {
                      "name": 178482
                    }
                  ]
                },
                {
                  "name": 58794
                },
                {
                  "name": 25268
                },
                {
                  "name": 260854
                },
                {
                  "name": 122371
                },
                {
                  "name": 200162
                },
                {
                  "name": 16750
                },
                {
                  "name": 130217
                },
                {
                  "name": 40944
                }
              ]
            },
            {
              "name": 189041,
              "children": [
                {
                  "name": 226459,
                  "children": [
                    {
                      "name": 160323
                    },
                    {
                      "name": 136862
                    }
                  ]
                },
                {
                  "name": 7204,
                  "children": [
                    {
                      "name": 25678
                    },
                    {
                      "name": 89886
                    },
                    {
                      "name": 13716
                    },
                    {
                      "name": 36935
                    },
                    {
                      "name": 128560
                    },
                    {
                      "name": 184796
                    },
                    {
                      "name": 153571
                    },
                    {
                      "name": 60730
                    },
                    {
                      "name": 124809
                    }
                  ]
                },
                {
                  "name": 38659,
                  "children": [
                    {
                      "name": 110197
                    },
                    {
                      "name": 169498
                    },
                    {
                      "name": 100837
                    },
                    {
                      "name": 30426
                    },
                    {
                      "name": 10912
                    },
                    {
                      "name": 27115
                    },
                    {
                      "name": 89513
                    }
                  ]
                },
                {
                  "name": 26051
                }
              ]
            },
            {
              "name": 76219,
              "children": [
                {
                  "name": 210821
                },
                {
                  "name": 237462
                },
                {
                  "name": 259256
                },
                {
                  "name": 43969
                },
                {
                  "name": 106656
                },
                {
                  "name": 27708
                },
                {
                  "name": 33298
                },
                {
                  "name": 166577,
                  "children": [
                    {
                      "name": 94357
                    },
                    {
                      "name": 72555
                    },
                    {
                      "name": 73020
                    },
                    {
                      "name": 127722
                    }
                  ]
                },
                {
                  "name": 207882
                },
                {
                  "name": 16979
                },
                {
                  "name": 136857
                },
                {
                  "name": 25994
                }
              ]
            }
          ]
        },
        {
          "name": 219641,
          "children": [
            {
              "name": 226106
            },
            {
              "name": 267419
            },
            {
              "name": 208134
            },
            {
              "name": 37770
            },
            {
              "name": 128443
            },
            {
              "name": 119843
            }
          ]
        },
        {
          "name": 7770,
          "children": [
            {
              "name": 206255,
              "children": [
                {
                  "name": 168822
                },
                {
                  "name": 22216
                },
                {
                  "name": 132779
                },
                {
                  "name": 205096
                }
              ]
            },
            {
              "name": 141185,
              "children": [
                {
                  "name": 44169,
                  "children": [
                    {
                      "name": 27475
                    },
                    {
                      "name": 24854
                    },
                    {
                      "name": 212057
                    },
                    {
                      "name": 2847
                    },
                    {
                      "name": 185935,
                      "children": [
                        {
                          "name": 84914
                        },
                        {
                          "name": 222610
                        },
                        {
                          "name": 110986
                        },
                        {
                          "name": 20019
                        },
                        {
                          "name": 9622
                        },
                        {
                          "name": 153349
                        },
                        {
                          "name": 5107
                        },
                        {
                          "name": 133406
                        }
                      ]
                    },
                    {
                      "name": 257863,
                      "children": [
                        {
                          "name": 203225
                        }
                      ]
                    },
                    {
                      "name": 164
                    },
                    {
                      "name": 241118
                    },
                    {
                      "name": 257225
                    },
                    {
                      "name": 159794
                    },
                    {
                      "name": 126000
                    },
                    {
                      "name": 10723
                    },
                    {
                      "name": 225646
                    }
                  ]
                },
                {
                  "name": 24614,
                  "children": [
                    {
                      "name": 40858
                    },
                    {
                      "name": 60945
                    },
                    {
                      "name": 102
                    },
                    {
                      "name": 116850
                    },
                    {
                      "name": 37887
                    },
                    {
                      "name": 241011
                    },
                    {
                      "name": 103300,
                      "children": [
                        {
                          "name": 108436
                        },
                        {
                          "name": 113708,
                          "children": [
                            {
                              "name": 142122
                            }
                          ]
                        },
                        {
                          "name": 254720
                        }
                      ]
                    },
                    {
                      "name": 98056
                    },
                    {
                      "name": 67988
                    },
                    {
                      "name": 24135
                    },
                    {
                      "name": 91858
                    },
                    {
                      "name": 213122
                    },
                    {
                      "name": 187445
                    }
                  ]
                }
              ]
            },
            {
              "name": 178396,
              "children": [
                {
                  "name": 58512
                },
                {
                  "name": 100087
                },
                {
                  "name": 223626
                },
                {
                  "name": 121843
                },
                {
                  "name": 231568
                },
                {
                  "name": 166763
                },
                {
                  "name": 259218
                },
                {
                  "name": 175896
                },
                {
                  "name": 151838
                },
                {
                  "name": 242092
                },
                {
                  "name": 266551
                },
                {
                  "name": 56692
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "name": 105106,
      "children": [
        {
          "name": 26010
        },
        {
          "name": 88311
        }
      ]
    },
    {
      "name": 72520,
      "children": [
        {
          "name": 60212,
          "children": [
            {
              "name": 197896,
              "children": [
                {
                  "name": 90511
                },
                {
                  "name": 108581
                },
                {
                  "name": 125335
                },
                {
                  "name": 118677
                },
                {
                  "name": 77931
                },
                {
                  "name": 200897
                },
                {
                  "name": 160045
                },
                {
                  "name": 80148
                },
                {
                  "name": 162661
                }
              ]
            },
            {
              "name": 169058,
              "children": [
                {
                  "name": 228705
                },
                {
                  "name": 103949
                },
                {
                  "name": 173836
                },
                {
                  "name": 160009
                },
                {
                  "name": 112274
                },
                {
                  "name": 163294
                },
                {
                  "name": 202596
                }
              ]
            },
            {
              "name": 231432,
              "children": [
                {
                  "name": 239222
                },
                {
                  "name": 1212
                },
                {
                  "name": 214647
                },
                {
                  "name": 92145
                },
                {
                  "name": 228647
                },
                {
                  "name": 155005
                },
                {
                  "name": 47530,
                  "children": [
                    {
                      "name": 65881
                    },
                    {
                      "name": 180392
                    }
                  ]
                },
                {
                  "name": 14510,
                  "children": [
                    {
                      "name": 121205
                    },
                    {
                      "name": 89113
                    },
                    {
                      "name": 242000
                    },
                    {
                      "name": 260143
                    },
                    {
                      "name": 64901
                    },
                    {
                      "name": 232237
                    },
                    {
                      "name": 225910
                    },
                    {
                      "name": 237546
                    },
                    {
                      "name": 124907
                    },
                    {
                      "name": 13911
                    },
                    {
                      "name": 242411
                    },
                    {
                      "name": 260892
                    },
                    {
                      "name": 4162
                    },
                    {
                      "name": 212350
                    },
                    {
                      "name": 167704
                    },
                    {
                      "name": 237976
                    },
                    {
                      "name": 171493
                    },
                    {
                      "name": 189445
                    },
                    {
                      "name": 255516
                    },
                    {
                      "name": 160100
                    },
                    {
                      "name": 264370
                    },
                    {
                      "name": 98983
                    },
                    {
                      "name": 241949
                    },
                    {
                      "name": 192301
                    },
                    {
                      "name": 257463
                    },
                    {
                      "name": 198899
                    },
                    {
                      "name": 83936
                    },
                    {
                      "name": 242514
                    },
                    {
                      "name": 126797
                    },
                    {
                      "name": 182972
                    },
                    {
                      "name": 218455
                    },
                    {
                      "name": 194854
                    }
                  ]
                },
                {
                  "name": 197314
                },
                {
                  "name": 196288
                },
                {
                  "name": 238412
                },
                {
                  "name": 134059,
                  "children": [
                    {
                      "name": 87117
                    },
                    {
                      "name": 46616
                    },
                    {
                      "name": 69299
                    },
                    {
                      "name": 188400
                    },
                    {
                      "name": 201968
                    }
                  ]
                },
                {
                  "name": 182710,
                  "children": [
                    {
                      "name": 157114
                    },
                    {
                      "name": 176229
                    },
                    {
                      "name": 182622
                    },
                    {
                      "name": 126176
                    },
                    {
                      "name": 71567
                    },
                    {
                      "name": 212238
                    },
                    {
                      "name": 188978
                    },
                    {
                      "name": 22643
                    },
                    {
                      "name": 23478
                    },
                    {
                      "name": 259164
                    },
                    {
                      "name": 163995
                    },
                    {
                      "name": 37111
                    },
                    {
                      "name": 72499
                    },
                    {
                      "name": 251771
                    },
                    {
                      "name": 124034
                    },
                    {
                      "name": 106735
                    },
                    {
                      "name": 42931
                    },
                    {
                      "name": 80892
                    },
                    {
                      "name": 191032
                    },
                    {
                      "name": 4118
                    },
                    {
                      "name": 222832
                    },
                    {
                      "name": 8382
                    },
                    {
                      "name": 267478
                    },
                    {
                      "name": 177894
                    },
                    {
                      "name": 253367
                    },
                    {
                      "name": 113202
                    }
                  ]
                },
                {
                  "name": 51872
                },
                {
                  "name": 121271
                },
                {
                  "name": 139960
                }
              ]
            },
            {
              "name": 160884,
              "children": [
                {
                  "name": 185350,
                  "children": [
                    {
                      "name": 261303
                    },
                    {
                      "name": 47624
                    },
                    {
                      "name": 139792
                    },
                    {
                      "name": 251012
                    },
                    {
                      "name": 120870
                    },
                    {
                      "name": 177913
                    },
                    {
                      "name": 198508
                    },
                    {
                      "name": 181974
                    },
                    {
                      "name": 253511
                    }
                  ]
                },
                {
                  "name": 218616,
                  "children": [
                    {
                      "name": 176661
                    },
                    {
                      "name": 182606
                    },
                    {
                      "name": 88560
                    },
                    {
                      "name": 139225
                    },
                    {
                      "name": 1966
                    },
                    {
                      "name": 231604
                    }
                  ]
                },
                {
                  "name": 98387,
                  "children": [
                    {
                      "name": 238354
                    },
                    {
                      "name": 102312
                    },
                    {
                      "name": 101901
                    },
                    {
                      "name": 48102
                    },
                    {
                      "name": 194048
                    },
                    {
                      "name": 105890
                    }
                  ]
                }
              ]
            },
            {
              "name": 77119,
              "children": [
                {
                  "name": 16008
                },
                {
                  "name": 236926
                },
                {
                  "name": 168175
                },
                {
                  "name": 126471,
                  "children": [
                    {
                      "name": 186652
                    },
                    {
                      "name": 76180
                    },
                    {
                      "name": 145277
                    },
                    {
                      "name": 5753,
                      "children": [
                        {
                          "name": 259189
                        }
                      ]
                    },
                    {
                      "name": 43975
                    },
                    {
                      "name": 7110
                    },
                    {
                      "name": 227532,
                      "children": [
                        {
                          "name": 51381
                        }
                      ]
                    },
                    {
                      "name": 72809
                    }
                  ]
                },
                {
                  "name": 23681
                },
                {
                  "name": 176384
                },
                {
                  "name": 260443
                },
                {
                  "name": 241623
                }
              ]
            }
          ]
        },
        {
          "name": 17625,
          "children": [
            {
              "name": 129353,
              "children": [
                {
                  "name": 179949
                },
                {
                  "name": 57608
                },
                {
                  "name": 178635
                },
                {
                  "name": 244347
                },
                {
                  "name": 225427
                },
                {
                  "name": 29230,
                  "children": [
                    {
                      "name": 238276
                    }
                  ]
                },
                {
                  "name": 192595
                },
                {
                  "name": 23688,
                  "children": [
                    {
                      "name": 84127
                    }
                  ]
                },
                {
                  "name": 172247
                },
                {
                  "name": 65715,
                  "children": [
                    {
                      "name": 82719
                    }
                  ]
                },
                {
                  "name": 137754
                }
              ]
            },
            {
              "name": 217987,
              "children": [
                {
                  "name": 160004
                },
                {
                  "name": 205530
                },
                {
                  "name": 98211
                },
                {
                  "name": 222905
                },
                {
                  "name": 50768
                },
                {
                  "name": 255912
                },
                {
                  "name": 217231
                },
                {
                  "name": 131584
                },
                {
                  "name": 219164
                }
              ]
            },
            {
              "name": 95636,
              "children": [
                {
                  "name": 14277,
                  "children": [
                    {
                      "name": 228262
                    },
                    {
                      "name": 189258
                    },
                    {
                      "name": 46458
                    },
                    {
                      "name": 202149
                    },
                    {
                      "name": 42069
                    }
                  ]
                },
                {
                  "name": 211599,
                  "children": [
                    {
                      "name": 166132
                    },
                    {
                      "name": 47265
                    },
                    {
                      "name": 49065
                    },
                    {
                      "name": 116213
                    },
                    {
                      "name": 261997
                    },
                    {
                      "name": 259480
                    },
                    {
                      "name": 5521
                    }
                  ]
                },
                {
                  "name": 89158
                }
              ]
            },
            {
              "name": 173369,
              "children": [
                {
                  "name": 80229,
                  "children": [
                    {
                      "name": 86835
                    },
                    {
                      "name": 142949
                    },
                    {
                      "name": 166144
                    },
                    {
                      "name": 44445,
                      "children": [
                        {
                          "name": 142740
                        },
                        {
                          "name": 124618
                        },
                        {
                          "name": 238947
                        },
                        {
                          "name": 135645
                        },
                        {
                          "name": 67277
                        },
                        {
                          "name": 155523
                        },
                        {
                          "name": 216455
                        },
                        {
                          "name": 213438
                        },
                        {
                          "name": 135972
                        },
                        {
                          "name": 256817
                        },
                        {
                          "name": 225207
                        }
                      ]
                    },
                    {
                      "name": 36162
                    },
                    {
                      "name": 83549
                    },
                    {
                      "name": 31510
                    },
                    {
                      "name": 265089
                    },
                    {
                      "name": 100364
                    },
                    {
                      "name": 157650
                    },
                    {
                      "name": 76346
                    },
                    {
                      "name": 221882
                    },
                    {
                      "name": 209961
                    },
                    {
                      "name": 250701
                    },
                    {
                      "name": 145846
                    },
                    {
                      "name": 60749
                    },
                    {
                      "name": 14427
                    },
                    {
                      "name": 112241
                    }
                  ]
                },
                {
                  "name": 21187
                },
                {
                  "name": 86773
                },
                {
                  "name": 179139
                }
              ]
            }
          ]
        },
        {
          "name": 116574,
          "children": [
            {
              "name": 68000
            },
            {
              "name": 266061,
              "children": [
                {
                  "name": 60015
                },
                {
                  "name": 143768
                },
                {
                  "name": 61009
                },
                {
                  "name": 182962
                },
                {
                  "name": 31094
                },
                {
                  "name": 167895
                },
                {
                  "name": 54158
                },
                {
                  "name": 41174
                }
              ]
            },
            {
              "name": 49598,
              "children": [
                {
                  "name": 111887
                },
                {
                  "name": 21813
                },
                {
                  "name": 157012
                },
                {
                  "name": 10078
                },
                {
                  "name": 6801
                },
                {
                  "name": 122743
                },
                {
                  "name": 106166
                },
                {
                  "name": 133765
                },
                {
                  "name": 137606
                },
                {
                  "name": 22727
                },
                {
                  "name": 126513
                },
                {
                  "name": 62398
                },
                {
                  "name": 94588
                },
                {
                  "name": 158511
                },
                {
                  "name": 75717
                },
                {
                  "name": 110372
                },
                {
                  "name": 154134
                },
                {
                  "name": 49209
                },
                {
                  "name": 53633
                },
                {
                  "name": 57951
                },
                {
                  "name": 37108
                },
                {
                  "name": 38802
                },
                {
                  "name": 87705
                }
              ]
            },
            {
              "name": 160797
            }
          ]
        },
        {
          "name": 181864,
          "children": [
            {
              "name": 86094,
              "children": [
                {
                  "name": 34360
                },
                {
                  "name": 110283
                },
                {
                  "name": 21092
                },
                {
                  "name": 257253
                },
                {
                  "name": 63974
                },
                {
                  "name": 49242
                }
              ]
            },
            {
              "name": 53137,
              "children": [
                {
                  "name": 132518,
                  "children": [
                    {
                      "name": 241039
                    },
                    {
                      "name": 100767
                    },
                    {
                      "name": 189233
                    },
                    {
                      "name": 155896
                    },
                    {
                      "name": 146476
                    },
                    {
                      "name": 132440
                    },
                    {
                      "name": 124367
                    },
                    {
                      "name": 127410
                    },
                    {
                      "name": 113673
                    },
                    {
                      "name": 107528
                    },
                    {
                      "name": 89107
                    },
                    {
                      "name": 183589
                    },
                    {
                      "name": 174305
                    },
                    {
                      "name": 174314
                    },
                    {
                      "name": 82677
                    },
                    {
                      "name": 82698
                    },
                    {
                      "name": 119004
                    },
                    {
                      "name": 249657
                    },
                    {
                      "name": 96852
                    },
                    {
                      "name": 180379
                    },
                    {
                      "name": 68602
                    },
                    {
                      "name": 26046
                    },
                    {
                      "name": 210698
                    },
                    {
                      "name": 161940
                    },
                    {
                      "name": 215645
                    },
                    {
                      "name": 142313
                    },
                    {
                      "name": 251846
                    },
                    {
                      "name": 199427
                    },
                    {
                      "name": 150313
                    },
                    {
                      "name": 202557
                    },
                    {
                      "name": 92447
                    },
                    {
                      "name": 106108
                    },
                    {
                      "name": 181192
                    },
                    {
                      "name": 162853
                    },
                    {
                      "name": 245368
                    },
                    {
                      "name": 163709
                    },
                    {
                      "name": 8083
                    },
                    {
                      "name": 233168
                    },
                    {
                      "name": 256948
                    },
                    {
                      "name": 34339
                    },
                    {
                      "name": 249333
                    },
                    {
                      "name": 213203
                    },
                    {
                      "name": 143675
                    },
                    {
                      "name": 145347
                    },
                    {
                      "name": 100709
                    },
                    {
                      "name": 238662
                    },
                    {
                      "name": 207772
                    },
                    {
                      "name": 130528
                    },
                    {
                      "name": 52052
                    },
                    {
                      "name": 8202
                    },
                    {
                      "name": 99488
                    },
                    {
                      "name": 130545
                    },
                    {
                      "name": 281
                    },
                    {
                      "name": 152434
                    },
                    {
                      "name": 13435
                    },
                    {
                      "name": 85436
                    },
                    {
                      "name": 61870
                    },
                    {
                      "name": 241100
                    },
                    {
                      "name": 3847
                    },
                    {
                      "name": 23572
                    },
                    {
                      "name": 67632
                    },
                    {
                      "name": 74358
                    },
                    {
                      "name": 253215
                    },
                    {
                      "name": 152436
                    },
                    {
                      "name": 95247
                    },
                    {
                      "name": 57494
                    },
                    {
                      "name": 42985
                    },
                    {
                      "name": 141243
                    },
                    {
                      "name": 249142
                    },
                    {
                      "name": 17336
                    },
                    {
                      "name": 87426
                    },
                    {
                      "name": 54260
                    },
                    {
                      "name": 47366
                    },
                    {
                      "name": 24753
                    },
                    {
                      "name": 148882
                    },
                    {
                      "name": 124489
                    },
                    {
                      "name": 17076
                    },
                    {
                      "name": 20212
                    },
                    {
                      "name": 2200
                    },
                    {
                      "name": 195119
                    },
                    {
                      "name": 134249
                    },
                    {
                      "name": 204581
                    },
                    {
                      "name": 242577
                    },
                    {
                      "name": 193069
                    },
                    {
                      "name": 143946
                    },
                    {
                      "name": 136497
                    },
                    {
                      "name": 41934
                    },
                    {
                      "name": 77459
                    }
                  ]
                },
                {
                  "name": 176757,
                  "children": [
                    {
                      "name": 106649,
                      "children": [
                        {
                          "name": 67495
                        }
                      ]
                    },
                    {
                      "name": 176415,
                      "children": [
                        {
                          "name": 22588
                        },
                        {
                          "name": 208097,
                          "children": [
                            {
                              "name": 257668
                            },
                            {
                              "name": 52390
                            },
                            {
                              "name": 188975
                            },
                            {
                              "name": 48397
                            },
                            {
                              "name": 79807
                            },
                            {
                              "name": 152158
                            },
                            {
                              "name": 129443
                            }
                          ]
                        },
                        {
                          "name": 160393
                        },
                        {
                          "name": 35783
                        }
                      ]
                    },
                    {
                      "name": 195630,
                      "children": [
                        {
                          "name": 116660
                        },
                        {
                          "name": 121680
                        },
                        {
                          "name": 245257
                        }
                      ]
                    }
                  ]
                },
                {
                  "name": 125746
                },
                {
                  "name": 38513
                },
                {
                  "name": 205041
                },
                {
                  "name": 79599
                },
                {
                  "name": 120803
                },
                {
                  "name": 169863,
                  "children": [
                    {
                      "name": 12559
                    },
                    {
                      "name": 215854
                    },
                    {
                      "name": 210475
                    },
                    {
                      "name": 112812
                    },
                    {
                      "name": 262316
                    },
                    {
                      "name": 54988
                    },
                    {
                      "name": 168451
                    },
                    {
                      "name": 158196
                    },
                    {
                      "name": 111256
                    },
                    {
                      "name": 124880
                    },
                    {
                      "name": 166463
                    },
                    {
                      "name": 245945
                    },
                    {
                      "name": 12587
                    },
                    {
                      "name": 77442
                    },
                    {
                      "name": 177502
                    },
                    {
                      "name": 158957
                    },
                    {
                      "name": 263087
                    },
                    {
                      "name": 199996
                    },
                    {
                      "name": 122946
                    },
                    {
                      "name": 234885
                    },
                    {
                      "name": 211329
                    },
                    {
                      "name": 69594
                    },
                    {
                      "name": 110699
                    },
                    {
                      "name": 190283
                    },
                    {
                      "name": 122369
                    },
                    {
                      "name": 167063
                    },
                    {
                      "name": 217409
                    },
                    {
                      "name": 124211
                    },
                    {
                      "name": 107978
                    },
                    {
                      "name": 30010
                    },
                    {
                      "name": 188352
                    },
                    {
                      "name": 43751
                    },
                    {
                      "name": 234866
                    },
                    {
                      "name": 248323
                    },
                    {
                      "name": 181290
                    },
                    {
                      "name": 141749
                    },
                    {
                      "name": 260966
                    },
                    {
                      "name": 30632
                    },
                    {
                      "name": 162851
                    },
                    {
                      "name": 254555
                    }
                  ]
                },
                {
                  "name": 243613
                },
                {
                  "name": 250251
                }
              ]
            },
            {
              "name": 128562,
              "children": [
                {
                  "name": 186227
                },
                {
                  "name": 15173
                },
                {
                  "name": 36371
                },
                {
                  "name": 42178
                },
                {
                  "name": 104914
                }
              ]
            },
            {
              "name": 240514
            },
            {
              "name": 191665,
              "children": [
                {
                  "name": 126514
                },
                {
                  "name": 94648,
                  "children": [
                    {
                      "name": 205795
                    },
                    {
                      "name": 198392
                    },
                    {
                      "name": 5961
                    },
                    {
                      "name": 121373
                    },
                    {
                      "name": 215652
                    },
                    {
                      "name": 23216
                    },
                    {
                      "name": 238445
                    },
                    {
                      "name": 223583
                    },
                    {
                      "name": 219544
                    }
                  ]
                },
                {
                  "name": 105964,
                  "children": [
                    {
                      "name": 62282,
                      "children": [
                        {
                          "name": 157073
                        }
                      ]
                    },
                    {
                      "name": 248697
                    },
                    {
                      "name": 141691
                    },
                    {
                      "name": 258729
                    },
                    {
                      "name": 223880
                    },
                    {
                      "name": 234868
                    }
                  ]
                },
                {
                  "name": 115829,
                  "children": [
                    {
                      "name": 111166
                    },
                    {
                      "name": 31984
                    },
                    {
                      "name": 47158
                    },
                    {
                      "name": 196744
                    },
                    {
                      "name": 125971
                    },
                    {
                      "name": 152324
                    },
                    {
                      "name": 20702
                    },
                    {
                      "name": 253448
                    },
                    {
                      "name": 184177
                    },
                    {
                      "name": 266542
                    },
                    {
                      "name": 23912
                    },
                    {
                      "name": 42160
                    }
                  ]
                },
                {
                  "name": 150921,
                  "children": [
                    {
                      "name": 181032
                    },
                    {
                      "name": 156752
                    },
                    {
                      "name": 166275
                    },
                    {
                      "name": 150361
                    },
                    {
                      "name": 169573
                    },
                    {
                      "name": 83232
                    },
                    {
                      "name": 40760
                    },
                    {
                      "name": 76004
                    },
                    {
                      "name": 105559
                    },
                    {
                      "name": 83120
                    },
                    {
                      "name": 143209
                    },
                    {
                      "name": 189134
                    },
                    {
                      "name": 66768
                    },
                    {
                      "name": 185675
                    },
                    {
                      "name": 252175
                    },
                    {
                      "name": 164079
                    },
                    {
                      "name": 122559
                    },
                    {
                      "name": 93279
                    },
                    {
                      "name": 126146
                    },
                    {
                      "name": 81595
                    },
                    {
                      "name": 201686
                    },
                    {
                      "name": 179331
                    },
                    {
                      "name": 217256
                    },
                    {
                      "name": 267150
                    }
                  ]
                },
                {
                  "name": 6458
                }
              ]
            },
            {
              "name": 98052,
              "children": [
                {
                  "name": 68972
                },
                {
                  "name": 193926
                },
                {
                  "name": 140320
                },
                {
                  "name": 215049
                },
                {
                  "name": 83398
                },
                {
                  "name": 31905
                },
                {
                  "name": 161792
                },
                {
                  "name": 231510
                },
                {
                  "name": 168295
                },
                {
                  "name": 3473
                },
                {
                  "name": 29734
                },
                {
                  "name": 224631
                },
                {
                  "name": 102880
                },
                {
                  "name": 42363
                },
                {
                  "name": 70444
                },
                {
                  "name": 156689
                },
                {
                  "name": 254794
                },
                {
                  "name": 242173
                },
                {
                  "name": 254250
                },
                {
                  "name": 248521
                },
                {
                  "name": 189909
                },
                {
                  "name": 200313
                },
                {
                  "name": 233332
                },
                {
                  "name": 20726
                },
                {
                  "name": 136593
                },
                {
                  "name": 5809
                },
                {
                  "name": 4041
                },
                {
                  "name": 240204
                }
              ]
            },
            {
              "name": 29747,
              "children": [
                {
                  "name": 172927
                },
                {
                  "name": 186417,
                  "children": [
                    {
                      "name": 80336
                    },
                    {
                      "name": 207286
                    },
                    {
                      "name": 250104
                    },
                    {
                      "name": 223305
                    },
                    {
                      "name": 153761
                    },
                    {
                      "name": 210127
                    },
                    {
                      "name": 54929
                    },
                    {
                      "name": 240738
                    },
                    {
                      "name": 188568
                    },
                    {
                      "name": 264757
                    },
                    {
                      "name": 194205
                    },
                    {
                      "name": 123046
                    },
                    {
                      "name": 160933
                    },
                    {
                      "name": 222532
                    },
                    {
                      "name": 241283
                    },
                    {
                      "name": 5705
                    },
                    {
                      "name": 74123
                    },
                    {
                      "name": 51231
                    },
                    {
                      "name": 176061
                    },
                    {
                      "name": 242101
                    },
                    {
                      "name": 78645
                    },
                    {
                      "name": 6627
                    },
                    {
                      "name": 95774
                    },
                    {
                      "name": 81306
                    },
                    {
                      "name": 25161
                    },
                    {
                      "name": 245333
                    },
                    {
                      "name": 135726
                    },
                    {
                      "name": 178716
                    },
                    {
                      "name": 157642
                    },
                    {
                      "name": 78236
                    },
                    {
                      "name": 181563
                    },
                    {
                      "name": 52034
                    },
                    {
                      "name": 105301
                    },
                    {
                      "name": 221865
                    },
                    {
                      "name": 116343
                    },
                    {
                      "name": 241101
                    },
                    {
                      "name": 163970
                    },
                    {
                      "name": 84698
                    },
                    {
                      "name": 98181
                    },
                    {
                      "name": 256601
                    }
                  ]
                },
                {
                  "name": 163100,
                  "children": [
                    {
                      "name": 111353
                    },
                    {
                      "name": 163301
                    },
                    {
                      "name": 153683
                    },
                    {
                      "name": 50707
                    },
                    {
                      "name": 127214
                    },
                    {
                      "name": 85718
                    },
                    {
                      "name": 48244
                    },
                    {
                      "name": 2793
                    },
                    {
                      "name": 240241
                    },
                    {
                      "name": 50150
                    },
                    {
                      "name": 169370
                    },
                    {
                      "name": 192685
                    },
                    {
                      "name": 117958
                    },
                    {
                      "name": 170171
                    },
                    {
                      "name": 50776
                    },
                    {
                      "name": 206145
                    },
                    {
                      "name": 205579
                    },
                    {
                      "name": 80651
                    },
                    {
                      "name": 80639
                    },
                    {
                      "name": 56322
                    },
                    {
                      "name": 47626
                    },
                    {
                      "name": 26307
                    },
                    {
                      "name": 85409
                    },
                    {
                      "name": 158909
                    },
                    {
                      "name": 158795
                    },
                    {
                      "name": 262292
                    },
                    {
                      "name": 80141
                    },
                    {
                      "name": 170201
                    },
                    {
                      "name": 64369
                    },
                    {
                      "name": 198868
                    },
                    {
                      "name": 257683
                    },
                    {
                      "name": 222996
                    },
                    {
                      "name": 194614
                    },
                    {
                      "name": 993
                    },
                    {
                      "name": 162846
                    },
                    {
                      "name": 192779
                    },
                    {
                      "name": 125751
                    },
                    {
                      "name": 149817
                    },
                    {
                      "name": 32098
                    },
                    {
                      "name": 2539
                    },
                    {
                      "name": 138695
                    },
                    {
                      "name": 204190
                    },
                    {
                      "name": 9650
                    },
                    {
                      "name": 35310
                    },
                    {
                      "name": 137668
                    },
                    {
                      "name": 65543
                    },
                    {
                      "name": 156127
                    },
                    {
                      "name": 147890
                    },
                    {
                      "name": 156305
                    },
                    {
                      "name": 2454
                    },
                    {
                      "name": 111405
                    },
                    {
                      "name": 135783
                    },
                    {
                      "name": 144559
                    },
                    {
                      "name": 90417
                    },
                    {
                      "name": 246669
                    },
                    {
                      "name": 50186
                    },
                    {
                      "name": 91339
                    },
                    {
                      "name": 187953
                    },
                    {
                      "name": 147913
                    },
                    {
                      "name": 7979
                    },
                    {
                      "name": 161082
                    },
                    {
                      "name": 107471
                    },
                    {
                      "name": 78188
                    },
                    {
                      "name": 182204
                    },
                    {
                      "name": 117962
                    },
                    {
                      "name": 219672
                    },
                    {
                      "name": 60366
                    },
                    {
                      "name": 73651
                    },
                    {
                      "name": 94540
                    },
                    {
                      "name": 202322
                    },
                    {
                      "name": 166616
                    },
                    {
                      "name": 79889
                    },
                    {
                      "name": 9680
                    },
                    {
                      "name": 66223
                    },
                    {
                      "name": 30428
                    },
                    {
                      "name": 149601
                    },
                    {
                      "name": 158226
                    },
                   {
                      "name": 150241
                    },
                    {
                      "name": 168182
                    },
                    {
                      "name": 223738
                    },
                    {
                      "name": 189266
                    },
                    {
                      "name": 139555
                    },
                    {
                      "name": 119852
                    },
                    {
                      "name": 169892
                    },
                    {
                      "name": 47900
                    },
                    {
                      "name": 86024
                    },
                    {
                      "name": 257639
                    },
                    {
                      "name": 104999
                    },
                    {
                      "name": 205955
                    },
                    {
                      "name": 233843
                    },
                    {
                      "name": 205391
                    },
                    {
                      "name": 113472
                    },
                    {
                      "name": 82967
                    },
                    {
                      "name": 233975
                    },
                    {
                      "name": 73140
                    },
                    {
                      "name": 83335
                    },
                    {
                      "name": 120669
                    },
                    {
                      "name": 153361
                    },
                    {
                      "name": 266226
                    },
                    {
                      "name": 96181
                    },
                    {
                      "name": 12101
                    },
                    {
                      "name": 73147
                    },
                    {
                      "name": 186941
                    },
                    {
                      "name": 139639
                    },
                    {
                      "name": 140390
                    },
                    {
                      "name": 129759
                    },
                    {
                      "name": 85300
                    },
                    {
                      "name": 50092
                    },
                    {
                      "name": 18939
                    },
                    {
                      "name": 105723
                    },
                    {
                      "name": 168236
                    },
                    {
                      "name": 132060
                    },
                    {
                      "name": 158959
                    },
                    {
                      "name": 169623
                    },
                    {
                      "name": 21311
                    },
                    {
                      "name": 139638
                    },
                    {
                      "name": 249613
                    },
                    {
                      "name": 169694
                    },
                    {
                      "name": 80451
                    },
                    {
                      "name": 138906
                    },
                    {
                      "name": 199213
                    },
                    {
                      "name": 19192
                    },
                    {
                      "name": 83313
                    },
                    {
                      "name": 7972
                    },
                    {
                      "name": 234944
                    },
                    {
                      "name": 129723
                    },
                    {
                      "name": 26832
                    },
                    {
                      "name": 58481
                    },
                    {
                      "name": 54572
                    },
                    {
                      "name": 145520
                    },
                    {
                      "name": 35983
                    },
                    {
                      "name": 65673
                    },
                    {
                      "name": 148890
                    },
                    {
                      "name": 225192
                    },
                    {
                      "name": 150821
                    },
                    {
                      "name": 179366
                    },
                    {
                      "name": 11860
                    },
                    {
                      "name": 39226
                    },
                    {
                      "name": 61981
                    },
                    {
                      "name": 131070
                    },
                    {
                      "name": 248656
                    },
                    {
                      "name": 48855
                    },
                    {
                      "name": 136335
                    },
                    {
                      "name": 159529
                    },
                    {
                      "name": 146154
                    },
                    {
                      "name": 172488
                    },
                    {
                      "name": 133730
                    },
                    {
                      "name": 136233
                    },
                    {
                      "name": 188686
                    },
                    {
                      "name": 48857
                    },
                    {
                      "name": 179404
                    },
                    {
                      "name": 257854
                    },
                    {
                      "name": 136869
                    },
                    {
                      "name": 45758
                    },
                    {
                      "name": 86859
                    },
                    {
                      "name": 88531
                    },
                    {
                      "name": 70483
                    },
                    {
                      "name": 102357
                    },
                    {
                      "name": 98779
                    },
                    {
                      "name": 240911
                    },
                    {
                      "name": 42351
                    },
                    {
                      "name": 225036
                    },
                    {
                      "name": 259435
                    },
                    {
                      "name": 219114
                    },
                    {
                      "name": 188905
                    },
                    {
                      "name": 43033
                    },
                    {
                      "name": 249971
                    },
                    {
                      "name": 183387
                    },
                    {
                      "name": 134619
                    },
                    {
                      "name": 183388
                    },
                    {
                      "name": 128790
                    },
                    {
                      "name": 23940
                    },
                    {
                      "name": 164524
                    },
                    {
                      "name": 162175
                    },
                    {
                      "name": 11712
                    },
                    {
                      "name": 156790
                    },
                    {
                      "name": 124160
                    },
                    {
                      "name": 56753
                    },
                    {
                      "name": 191710
                    },
                    {
                      "name": 144124
                    },
                    {
                      "name": 241106
                    },
                    {
                      "name": 145936
                    },
                    {
                      "name": 214000
                    },
                    {
                      "name": 152207
                    },
                    {
                      "name": 11827
                    },
                    {
                      "name": 149057
                    },
                    {
                      "name": 18635
                    },
                    {
                      "name": 160429
                    },
                    {
                      "name": 209144
                    },
                    {
                      "name": 244739
                    },
                    {
                      "name": 49072
                    },
                    {
                      "name": 254336
                    },
                    {
                      "name": 241940
                    },
                    {
                      "name": 197192
                    },
                    {
                      "name": 72250
                    },
                    {
                      "name": 74579
                    },
                    {
                      "name": 175078
                    },
                    {
                      "name": 244776
                    },
                    {
                      "name": 209869
                    },
                    {
                      "name": 116861
                    },
                    {
                      "name": 53130
                    },
                    {
                      "name": 106709
                    },
                    {
                      "name": 135525
                    },
                    {
                      "name": 141027
                    },
                    {
                      "name": 33782
                    },
                    {
                      "name": 79156
                    },
                    {
                      "name": 254384
                    },
                    {
                      "name": 45429
                    },
                    {
                      "name": 197662
                    },
                    {
                      "name": 262752
                    },
                    {
                      "name": 261835
                    },
                    {
                      "name": 183967
                    },
                    {
                      "name": 2209
                    },
                    {
                      "name": 79487
                    },
                    {
                      "name": 48886
                    },
                    {
                      "name": 22613
                    },
                    {
                      "name": 265317
                    },
                    {
                      "name": 243459
                    },
                    {
                      "name": 243744
                    },
                    {
                      "name": 49784
                    },
                    {
                      "name": 190546
                    },
                    {
                      "name": 5613
                    },
                    {
                      "name": 221773
                    },
                    {
                      "name": 51846
                    },
                    {
                      "name": 122169
                    },
                    {
                      "name": 65875
                    },
                    {
                      "name": 191591
                    },
                    {
                      "name": 44621
                    },
                    {
                      "name": 214042
                    },
                    {
                      "name": 225892
                    },
                    {
                      "name": 106204
                    },
                    {
                      "name": 11507
                    },
                    {
                      "name": 152122
                    },
                    {
                      "name": 69362
                    },
                    {
                      "name": 102148
                    },
                    {
                      "name": 15137
                    },
                    {
                      "name": 57640
                    },
                    {
                      "name": 141605
                    },
                    {
                      "name": 137261
                    },
                    {
                      "name": 51640
                    },
                    {
                      "name": 221543
                    },
                    {
                      "name": 148691
                    },
                    {
                      "name": 266885
                    },
                    {
                      "name": 90175
                    },
                    {
                      "name": 110015
                    },
                    {
                      "name": 146903
                    },
                    {
                      "name": 241714
                    },
                    {
                      "name": 123521
                    },
                    {
                      "name": 185552
                    },
                    {
                      "name": 100321
                    },
                    {
                      "name": 61455
                    },
                    {
                      "name": 101385
                    },
                    {
                      "name": 158550
                    },
                    {
                      "name": 159626
                    },
                    {
                      "name": 238986
                    },
                    {
                      "name": 180466
                    },
                    {
                      "name": 39429
                    },
                    {
                      "name": 99158
                    },
                    {
                      "name": 167899
                    },
                    {
                      "name": 185108
                    },
                    {
                      "name": 241366
                    },
                    {
                      "name": 22609
                    },
                    {
                      "name": 114503
                    },
                    {
                      "name": 55798
                    },
                    {
                      "name": 255759
                    },
                    {
                      "name": 34383
                    },
                    {
                      "name": 127572
                    },
                    {
                      "name": 219449
                    },
                    {
                      "name": 109114
                    },
                    {
                      "name": 12481
                    },
                    {
                      "name": 226961
                    },
                    {
                      "name": 14486
                    },
                    {
                      "name": 232370
                    },
                    {
                      "name": 122999
                    },
                    {
                      "name": 18984
                    },
                    {
                      "name": 67432
                    },
                    {
                      "name": 151449
                    },
                    {
                      "name": 197416
                    },
                    {
                      "name": 62743
                    },
                    {
                      "name": 54167
                    },
                    {
                      "name": 35921
                    },
                    {
                      "name": 90287
                    },
                    {
                      "name": 35595
                    },
                    {
                      "name": 93397
                    },
                    {
                      "name": 204347
                    },
                    {
                      "name": 159176
                    },
                    {
                      "name": 14642
                    },
                    {
                      "name": 20097
                    },
                    {
                      "name": 224190
                    },
                    {
                      "name": 128590
                    },
                    {
                      "name": 222086
                    },
                    {
                      "name": 52977
                    },
                    {
                      "name": 33607
                    },
                    {
                      "name": 52617
                    },
                    {
                      "name": 97430
                    },
                    {
                      "name": 263994
                    },
                    {
                      "name": 161926
                    },
                    {
                      "name": 138327
                    },
                    {
                      "name": 93301
                    },
                    {
                      "name": 151270
                    },
                    {
                      "name": 264122
                    },
                    {
                      "name": 114130
                    },
                    {
                      "name": 123449
                    },
                    {
                      "name": 245205
                    },
                    {
                      "name": 144664
                    },
                    {
                      "name": 38323
                    },
                    {
                      "name": 157355
                    },
                    {
                      "name": 17099
                    },
                    {
                      "name": 180847
                    },
                    {
                      "name": 171954
                    },
                    {
                      "name": 100145
                    },
                    {
                      "name": 101122
                    },
                    {
                      "name": 13732
                    },
                    {
                      "name": 174562
                    },
                    {
                      "name": 23824
                    },
                    {
                      "name": 81791
                    },
                    {
                      "name": 210620
                    },
                    {
                      "name": 198095
                    },
                    {
                      "name": 191320
                    },
                    {
                      "name": 3250
                    },
                    {
                      "name": 184917
                    },
                    {
                      "name": 8372
                    },
                    {
                      "name": 131435
                    },
                    {
                      "name": 170682
                    },
                    {
                      "name": 28505
                    },
                    {
                      "name": 53002
                    },
                    {
                      "name": 141100
                    },
                    {
                      "name": 255084
                    },
                    {
                      "name": 55672
                    },
                    {
                      "name": 31039
                    },
                    {
                      "name": 89966
                    },
                    {
                      "name": 61330
                    },
                    {
                      "name": 102986
                    },
                    {
                      "name": 84555
                    },
                    {
                      "name": 42225
                    }
                  ]
                },
                {
                  "name": 85821,
                  "children": [
                    {
                      "name": 231821
                    },
                    {
                      "name": 166020
                    },
                    {
                      "name": 118134
                    },
                    {
                      "name": 17994
                    },
                    {
                      "name": 160975
                    },
                    {
                      "name": 222584
                    },
                    {
                      "name": 8539
                    },
                    {
                      "name": 69687
                    },
                    {
                      "name": 69683
                    },
                    {
                      "name": 112763
                    },
                    {
                      "name": 84737
                    },
                    {
                      "name": 63370
                    },
                    {
                      "name": 203446
                    },
                    {
                      "name": 242873
                    },
                    {
                      "name": 140148
                    },
                    {
                      "name": 116047
                    },
                    {
                      "name": 66316
                    },
                    {
                      "name": 221254
                    },
                    {
                      "name": 248034
                    },
                    {
                      "name": 59359
                    },
                    {
                      "name": 109703
                    },
                    {
                      "name": 188525
                    },
                    {
                      "name": 147764
                    },
                    {
                      "name": 210093
                    },
                    {
                      "name": 254540
                    },
                    {
                      "name": 198170
                    },
                    {
                      "name": 37479
                    },
                    {
                      "name": 247927
                    },
                    {
                      "name": 64756
                    },
                    {
                      "name": 130101
                    },
                    {
                      "name": 235949
                    },
                    {
                      "name": 206851
                    },
                    {
                      "name": 135524
                    },
                    {
                      "name": 222790
                    },
                    {
                      "name": 115214
                    },
                    {
                      "name": 188027
                    },
                    {
                      "name": 142815
                    },
                    {
                      "name": 264975
                    },
                    {
                      "name": 206878
                    },
                    {
                      "name": 130742
                    },
                    {
                      "name": 238713
                    },
                    {
                      "name": 81206
                    },
                    {
                      "name": 182764
                    },
                    {
                      "name": 190396
                    },
                    {
                      "name": 184783
                    },
                    {
                      "name": 117125
                    },
                    {
                      "name": 16656
                    },
                    {
                      "name": 230818
                    },
                    {
                      "name": 173702
                    },
                    {
                      "name": 16025
                    },
                    {
                      "name": 262058
                    },
                    {
                      "name": 26767
                    },
                    {
                      "name": 124023
                    },
                    {
                      "name": 68317
                    },
                    {
                      "name": 263094
                    },
                    {
                      "name": 195510
                    },
                    {
                      "name": 2013
                    },
                    {
                      "name": 118143
                    },
                    {
                      "name": 204288
                    },
                    {
                      "name": 247205
                    },
                    {
                      "name": 20993
                    },
                    {
                      "name": 263278
                    },
                    {
                      "name": 94511
                    },
                    {
                      "name": 103658
                    },
                    {
                      "name": 167194
                    },
                    {
                      "name": 185011
                    },
                    {
                      "name": 29773
                    },
                    {
                      "name": 163727
                    },
                    {
                      "name": 8921
                    },
                    {
                      "name": 43622
                    },
                    {
                      "name": 240470
                    },
                    {
                      "name": 98708
                    },
                    {
                      "name": 16752
                    },
                    {
                      "name": 118942
                    },
                    {
                      "name": 145693
                    },
                    {
                      "name": 103629
                    },
                    {
                      "name": 207343
                    },
                    {
                      "name": 64766
                    },
                    {
                      "name": 148013
                    },
                    {
                      "name": 239322
                    },
                    {
                      "name": 179880
                    },
                    {
                      "name": 119730
                    },
                    {
                      "name": 207206
                    },
                    {
                      "name": 265030
                    },
                    {
                      "name": 114286
                    },
                    {
                      "name": 134539
                    },
                    {
                      "name": 34344
                    },
                    {
                      "name": 69558
                    },
                    {
                      "name": 131279
                    },
                    {
                      "name": 77219
                    },
                    {
                      "name": 265214
                    },
                    {
                      "name": 56297
                    },
                    {
                      "name": 94961
                    },
                    {
                      "name": 41798
                    },
                    {
                      "name": 122607
                    },
                    {
                      "name": 220147
                    },
                    {
                      "name": 188704
                    },
                    {
                      "name": 97032
                    },
                    {
                      "name": 239587
                    },
                    {
                      "name": 11200
                    },
                    {
                      "name": 91059
                    },
                    {
                      "name": 80551
                    },
                    {
                      "name": 25641
                    },
                    {
                      "name": 243109
                    },
                    {
                      "name": 92748
                    },
                    {
                      "name": 107591
                    },
                    {
                      "name": 218846
                    },
                    {
                      "name": 65497
                    },
                    {
                      "name": 115158
                    },
                    {
                      "name": 101884
                    },
                    {
                      "name": 227621
                    },
                    {
                      "name": 65423
                    },
                    {
                      "name": 32278
                    },
                    {
                      "name": 212133
                    },
                    {
                      "name": 196111
                    },
                    {
                      "name": 196154
                    },
                    {
                      "name": 160157
                    },
                    {
                      "name": 94667
                    },
                    {
                      "name": 154638
                    },
                    {
                      "name": 134171
                    },
                    {
                      "name": 57644
                    },
                    {
                      "name": 175839
                    },
                    {
                      "name": 121226
                    },
                    {
                      "name": 263985
                    },
                    {
                      "name": 120616
                    },
                    {
                      "name": 224078
                    },
                    {
                      "name": 9525
                    },
                    {
                      "name": 170306
                    },
                    {
                      "name": 73357
                    },
                    {
                      "name": 195989
                    },
                    {
                      "name": 91289
                    },
                    {
                      "name": 246024
                    },
                    {
                      "name": 53736
                    },
                    {
                      "name": 186397
                    },
                    {
                      "name": 241813
                    },
                    {
                      "name": 104221
                    },
                    {
                      "name": 188391
                    },
                    {
                      "name": 16695
                    },
                    {
                      "name": 59596
                    },
                    {
                      "name": 158451
                    },
                    {
                      "name": 241802
                    },
                    {
                      "name": 104642
                    },
                    {
                      "name": 127164
                    },
                    {
                      "name": 73959
                    },
                    {
                      "name": 246062
                    },
                    {
                      "name": 45803
                    },
                    {
                      "name": 180815
                    },
                    {
                      "name": 106233
                    },
                    {
                      "name": 265289
                    },
                    {
                      "name": 134473
                    },
                    {
                      "name": 68520
                    },
                    {
                      "name": 112132
                    },
                    {
                      "name": 47004
                    },
                    {
                      "name": 192138
                    },
                    {
                      "name": 169969
                    },
                    {
                      "name": 197820
                    },
                    {
                      "name": 227818
                    },
                    {
                      "name": 60880
                    },
                    {
                      "name": 214349
                    },
                    {
                      "name": 154578
                    },
                    {
                      "name": 121186
                    },
                    {
                      "name": 17357
                    },
                    {
                      "name": 40803
                    },
                    {
                      "name": 27236
                    },
                    {
                      "name": 43113
                    },
                    {
                      "name": 163560
                    },
                    {
                      "name": 132166
                    },
                    {
                      "name": 82226
                    },
                    {
                      "name": 84837
                    },
                    {
                      "name": 261527
                    },
                    {
                      "name": 158242
                    },
                    {
                      "name": 74522
                    },
                    {
                      "name": 198191
                    },
                    {
                      "name": 214390
                    },
                    {
                      "name": 79528
                    },
                    {
                      "name": 261273
                    },
                    {
                      "name": 225703
                    },
                    {
                      "name": 255703
                    },
                    {
                      "name": 251585
                    },
                    {
                      "name": 260216
                    },
                    {
                      "name": 22092
                    },
                    {
                      "name": 146404
                    },
                    {
                      "name": 126977
                    },
                    {
                      "name": 75007
                    },
                    {
                      "name": 242224
                    },
                    {
                      "name": 254478
                    },
                    {
                      "name": 140907
                    },
                    {
                      "name": 17798
                    },
                    {
                      "name": 25108
                    },
                    {
                      "name": 199076
                    }
                  ]
                },
                {
                  "name": 132615,
                  "children": [
                    {
                      "name": 149597
                    },
                    {
                      "name": 199348
                    }
                  ]
                },
                {
                  "name": 209551,
                  "children": [
                    {
                      "name": 11909
                    },
                    {
                      "name": 121224
                    },
                    {
                      "name": 220858
                    },
                    {
                      "name": 25495
                    },
                    {
                      "name": 121298
                    },
                    {
                      "name": 48330
                    },
                    {
                      "name": 124087
                    },
                    {
                      "name": 218942
                    },
                    {
                      "name": 51975
                    },
                    {
                      "name": 219198
                    },
                    {
                      "name": 25706
                    },
                    {
                      "name": 25723
                    },
                    {
                      "name": 183765
                    },
                    {
                      "name": 260060
                    },
                    {
                      "name": 214675
                    },
                    {
                      "name": 1894
                    },
                    {
                      "name": 51826
                    },
                    {
                      "name": 153598
                    },
                    {
                      "name": 33313
                    },
                    {
                      "name": 98028
                    },
                    {
                      "name": 157086
                    },
                    {
                      "name": 48790
                    },
                    {
                      "name": 223225
                    },
                    {
                      "name": 239972
                    },
                    {
                      "name": 11754
                    },
                    {
                      "name": 6200
                    },
                    {
                      "name": 50679
                    },
                    {
                      "name": 241379
                    },
                    {
                      "name": 159059
                    },
                    {
                      "name": 242872
                    },
                    {
                      "name": 253503
                    },
                    {
                      "name": 256597
                    },
                    {
                      "name": 215575
                    },
                    {
                      "name": 6006
                    },
                    {
                      "name": 185411
                    },
                    {
                      "name": 87788
                    },
                    {
                      "name": 216988
                    },
                    {
                      "name": 156595
                    },
                    {
                      "name": 219822
                    },
                    {
                      "name": 255364
                    },
                    {
                      "name": 6227
                    },
                    {
                      "name": 53464
                    },
                    {
                      "name": 96980
                    },
                    {
                      "name": 34641
                    },
                    {
                      "name": 151514
                    },
                    {
                      "name": 191400
                    },
                    {
                      "name": 186117
                    },
                    {
                      "name": 181623
                    },
                    {
                      "name": 124999
                    },
                    {
                      "name": 221271
                    },
                    {
                      "name": 177431
                    },
                    {
                      "name": 213662
                    },
                    {
                      "name": 93173
                    },
                    {
                      "name": 215793
                    },
                    {
                      "name": 185875
                    },
                    {
                      "name": 33526
                    },
                    {
                      "name": 119729
                    },
                    {
                      "name": 118166
                    },
                    {
                      "name": 95635
                    },
                    {
                      "name": 221889
                    },
                    {
                      "name": 88004
                    },
                    {
                      "name": 152208
                    },
                    {
                      "name": 253124
                    },
                    {
                      "name": 190470
                    },
                    {
                      "name": 48073
                    },
                    {
                      "name": 186866
                    },
                    {
                      "name": 237398
                    },
                    {
                      "name": 88641
                    },
                    {
                      "name": 120568
                    },
                    {
                      "name": 126020
                    },
                    {
                      "name": 216353
                    },
                    {
                      "name": 86250
                    },
                    {
                      "name": 113649
                    },
                    {
                      "name": 178568
                    },
                    {
                      "name": 51346
                    },
                    {
                      "name": 148171
                    },
                    {
                      "name": 177123
                    },
                    {
                      "name": 189187
                    },
                    {
                      "name": 158499
                    },
                    {
                      "name": 190584
                    },
                    {
                      "name": 124386
                    },
                    {
                      "name": 117891
                    },
                    {
                      "name": 90749
                    },
                    {
                      "name": 84122
                    },
                    {
                      "name": 154324
                    },
                    {
                      "name": 1857
                    },
                    {
                      "name": 219731
                    },
                    {
                      "name": 95192
                    },
                    {
                      "name": 97451
                    },
                    {
                      "name": 264786
                    },
                    {
                      "name": 90584
                    },
                    {
                      "name": 157827
                    },
                    {
                      "name": 31091
                    },
                    {
                      "name": 222704
                    },
                    {
                      "name": 55832
                    },
                    {
                      "name": 149208
                    },
                    {
                      "name": 151090
                    },
                    {
                      "name": 235531
                    },
                    {
                      "name": 53146
                    },
                    {
                      "name": 38121
                    },
                    {
                      "name": 128688
                    },
                    {
                      "name": 145233
                    },
                    {
                      "name": 36643
                    },
                    {
                      "name": 73377
                    },
                    {
                      "name": 18757
                    },
                    {
                      "name": 141226
                    },
                    {
                      "name": 80118
                    },
                    {
                      "name": 212793
                    },
                    {
                      "name": 230634
                    },
                    {
                      "name": 162287
                    },
                    {
                      "name": 14849
                    },
                    {
                      "name": 250816
                    },
                    {
                      "name": 37190
                    },
                    {
                      "name": 162975
                    },
                    {
                      "name": 144743
                    },
                    {
                      "name": 202324
                    },
                    {
                      "name": 101229
                    },
                    {
                      "name": 263223
                    },
                    {
                      "name": 69592
                    },
                    {
                      "name": 211995
                    },
                    {
                      "name": 113401
                    },
                    {
                      "name": 207699
                    },
                    {
                      "name": 72339
                    },
                    {
                      "name": 111417
                    },
                    {
                      "name": 130462
                    },
                    {
                      "name": 111108
                    },
                    {
                      "name": 263207
                    },
                    {
                      "name": 61319
                    },
                    {
                      "name": 5152
                    },
                    {
                      "name": 173317
                    },
                    {
                      "name": 38964
                    },
                    {
                      "name": 227832
                    },
                    {
                      "name": 136911
                    },
                    {
                      "name": 245374
                    },
                    {
                      "name": 164155
                    },
                    {
                      "name": 141815
                    },
                    {
                      "name": 109953
                    },
                    {
                      "name": 201067
                    },
                    {
                      "name": 199322
                    },
                    {
                      "name": 263365
                    },
                    {
                      "name": 161040
                    },
                    {
                      "name": 11280
                    },
                    {
                      "name": 21369
                    },
                    {
                      "name": 208225
                    },
                    {
                      "name": 8688
                    },
                    {
                      "name": 111063
                    },
                    {
                      "name": 106555
                    },
                    {
                      "name": 99523
                    },
                    {
                      "name": 137531
                    },
                    {
                      "name": 18154
                    },
                    {
                      "name": 131881
                    },
                    {
                      "name": 19289
                    },
                    {
                      "name": 227951
                    },
                    {
                      "name": 73262
                    },
                    {
                      "name": 108487
                    },
                    {
                      "name": 202998
                    },
                    {
                      "name": 58483
                    },
                    {
                      "name": 235032
                    },
                    {
                      "name": 40254
                    },
                    {
                      "name": 36120
                    },
                    {
                      "name": 137782
                    },
                    {
                      "name": 138135
                    },
                    {
                      "name": 233987
                    },
                    {
                      "name": 166088
                    },
                    {
                      "name": 107331
                    },
                    {
                      "name": 210430
                    },
                    {
                      "name": 202863
                    },
                    {
                      "name": 71569
                    },
                    {
                      "name": 163795
                    },
                    {
                      "name": 263713
                    },
                    {
                      "name": 172451
                    },
                    {
                      "name": 100960
                    },
                    {
                      "name": 227299
                    },
                    {
                      "name": 69019
                    },
                    {
                      "name": 131160
                    },
                    {
                      "name": 70423
                    },
                    {
                      "name": 17431
                    },
                    {
                      "name": 67868
                    },
                    {
                      "name": 100111
                    },
                    {
                      "name": 17174
                    },
                    {
                      "name": 16655
                    },
                    {
                      "name": 38064
                    },
                    {
                      "name": 167198
                    },
                    {
                      "name": 60027
                    },
                    {
                      "name": 195491
                    },
                    {
                      "name": 79538
                    },
                    {
                      "name": 245587
                    },
                    {
                      "name": 106405
                    },
                    {
                      "name": 100280
                    },
                    {
                      "name": 231494
                    },
                    {
                      "name": 227000
                    },
                    {
                      "name": 203647
                    },
                    {
                      "name": 63944
                    },
                    {
                      "name": 258771
                    },
                    {
                      "name": 72130
                    },
                    {
                      "name": 197807
                    },
                    {
                      "name": 161110
                    },
                    {
                      "name": 67787
                    },
                    {
                      "name": 170000
                    },
                    {
                      "name": 136347
                    },
                    {
                      "name": 62914
                    },
                    {
                      "name": 161454
                    },
                    {
                      "name": 17824
                    },
                    {
                      "name": 249402
                    },
                    {
                      "name": 146967
                    },
                    {
                      "name": 36794
                    },
                    {
                      "name": 257389
                    },
                    {
                      "name": 146671
                    },
                    {
                      "name": 209054
                    },
                    {
                      "name": 109592
                    },
                    {
                      "name": 244847
                    }
                  ]
                },
                {
                  "name": 96753,
                  "children": [
                    {
                      "name": 236483
                    }
                  ]
                },
                {
                  "name": 199405,
                  "children": [
                    {
                      "name": 71304
                    },
                    {
                      "name": 187420
                    },
                    {
                      "name": 141157
                    },
                    {
                      "name": 38462
                    },
                    {
                      "name": 32280
                    },
                    {
                      "name": 189191
                    },
                    {
                      "name": 100880
                    },
                    {
                      "name": 41401
                    },
                    {
                      "name": 3706
                    },
                    {
                      "name": 106603
                    },
                    {
                      "name": 30328
                    },
                    {
                      "name": 152416
                    },
                    {
                      "name": 55530
                    },
                    {
                      "name": 264
                    },
                    {
                      "name": 139645
                    },
                    {
                      "name": 107673
                    },
                    {
                      "name": 21675
                    },
                    {
                      "name": 154822
                    },
                    {
                      "name": 110958
                    },
                    {
                      "name": 65577
                    },
                    {
                      "name": 36571
                    },
                    {
                      "name": 52088
                    },
                    {
                      "name": 244197
                    },
                    {
                      "name": 45644
                    },
                    {
                      "name": 121949
                    },
                    {
                      "name": 78982
                    },
                    {
                      "name": 194704
                    },
                    {
                      "name": 148899
                    },
                    {
                      "name": 255409
                    },
                    {
                      "name": 232723
                    },
                    {
                      "name": 92440
                    },
                    {
                      "name": 79582
                    },
                    {
                      "name": 249735
                    },
                    {
                      "name": 106836
                    }
                  ]
                },
                {
                  "name": 196595,
                  "children": [
                    {
                      "name": 228589
                    },
                    {
                      "name": 31995
                    },
                    {
                      "name": 242711
                    },
                    {
                      "name": 204083
                    },
                    {
                      "name": 190395
                    },
                    {
                      "name": 105223
                    },
                    {
                      "name": 249656
                    },
                    {
                      "name": 235530
                    },
                    {
                      "name": 211903
                    },
                    {
                      "name": 87205
                    },
                    {
                      "name": 242845
                    },
                    {
                      "name": 71254
                    },
                    {
                      "name": 66742
                    },
                    {
                      "name": 243413
                    },
                    {
                      "name": 225643
                    },
                    {
                      "name": 260321
                    },
                    {
                      "name": 215648
                    },
                    {
                      "name": 265743
                    },
                    {
                      "name": 104771
                    },
                    {
                      "name": 100129
                    },
                    {
                      "name": 192389
                    },
                    {
                      "name": 121501
                    },
                    {
                      "name": 220448
                    },
                    {
                      "name": 3700
                    },
                    {
                      "name": 247857
                    },
                    {
                      "name": 151606
                    },
                    {
                      "name": 251359
                    },
                    {
                      "name": 22931
                    },
                    {
                      "name": 124273
                    },
                    {
                      "name": 220234
                    },
                    {
                      "name": 112123
                    },
                    {
                      "name": 170485
                    },
                    {
                      "name": 71602
                    },
                    {
                      "name": 66947
                    },
                    {
                      "name": 179566
                    },
                    {
                      "name": 53099
                    },
                    {
                      "name": 149634
                    },
                    {
                      "name": 52926
                    },
                    {
                      "name": 214906
                    },
                    {
                      "name": 63711
                    },
                    {
                      "name": 63001
                    },
                    {
                      "name": 23152
                    },
                    {
                      "name": 220633
                    },
                    {
                      "name": 80931
                    },
                    {
                      "name": 210054
                    },
                    {
                      "name": 11235
                    },
                    {
                      "name": 60257
                    },
                    {
                      "name": 219328
                    },
                    {
                      "name": 214092
                    },
                    {
                      "name": 22298
                    },
                    {
                      "name": 188018
                    },
                    {
                      "name": 61458
                    },
                    {
                      "name": 169433
                    },
                    {
                      "name": 72587
                    },
                    {
                      "name": 81182
                    },
                    {
                      "name": 1712
                    },
                    {
                      "name": 83298
                    },
                    {
                      "name": 1133
                    },
                    {
                      "name": 45124
                    },
                    {
                      "name": 105568
                    },
                    {
                      "name": 133079
                    },
                    {
                      "name": 38906
                    },
                    {
                      "name": 238929
                    },
                    {
                      "name": 20582
                    },
                    {
                      "name": 222725
                    },
                    {
                      "name": 35645
                    },
                    {
                      "name": 96762
                    },
                    {
                      "name": 198084
                    },
                    {
                      "name": 102883
                    },
                    {
                      "name": 78259
                    },
                    {
                      "name": 213928
                    },
                    {
                      "name": 38850
                    },
                    {
                      "name": 171473
                    },
                    {
                      "name": 248182
                    },
                    {
                      "name": 88688
                    },
                    {
                      "name": 56734
                    },
                    {
                      "name": 116668
                    },
                    {
                      "name": 145883
                    },
                    {
                      "name": 143754
                    },
                    {
                      "name": 165630
                    },
                    {
                      "name": 70174
                    },
                    {
                      "name": 147576
                    },
                    {
                      "name": 28216
                    },
                    {
                      "name": 224247
                    },
                    {
                      "name": 83854
                    },
                    {
                      "name": 122944
                    },
                    {
                      "name": 107964
                    },
                    {
                      "name": 113073
                    },
                    {
                      "name": 265674
                    },
                    {
                      "name": 237970
                    },
                    {
                      "name": 82257
                    },
                    {
                      "name": 250780
                    },
                    {
                      "name": 9748
                    },
                    {
                      "name": 52867
                    },
                    {
                      "name": 245138
                    },
                    {
                      "name": 75430
                    },
                    {
                      "name": 206648
                    },
                    {
                      "name": 219678
                    },
                    {
                     "name": 232466
                    },
                    {
                      "name": 97371
                    },
                    {
                      "name": 79881
                    },
                    {
                      "name": 115542
                    },
                    {
                      "name": 241232
                    },
                    {
                      "name": 149540
                    },
                    {
                      "name": 209478
                    },
                    {
                      "name": 168490
                    },
                    {
                      "name": 243236
                    },
                    {
                      "name": 160278
                    },
                    {
                      "name": 60683
                    },
                    {
                      "name": 232568
                    },
                    {
                      "name": 246370
                    },
                    {
                      "name": 138947
                    },
                    {
                      "name": 174633
                    },
                    {
                      "name": 231746
                    },
                    {
                      "name": 58204
                    },
                    {
                      "name": 256938
                    },
                    {
                      "name": 78597
                    },
                    {
                      "name": 213033
                    },
                    {
                      "name": 175619
                    },
                    {
                      "name": 251927
                    },
                    {
                      "name": 126370
                    }
                  ]
                }
              ]
            },
            {
              "name": 182920,
              "children": [
                {
                  "name": 221667,
                  "children": [
                    {
                      "name": 135651
                    }
                  ]
                },
                {
                  "name": 47403
                },
                {
                  "name": 102935
                },
                {
                  "name": 188483
                },
                {
                  "name": 27286
                },
                {
                  "name": 76093
                }
              ]
            },
            {
              "name": 210509,
              "children": [
                {
                  "name": 60380
                },
                {
                  "name": 267012
                },
                {
                  "name": 229984
                },
                {
                  "name": 100012
                }
              ]
            },
            {
              "name": 223316,
              "children": [
                {
                  "name": 56990
                },
                {
                  "name": 192275
                },
                {
                  "name": 133829,
                  "children": [
                    {
                      "name": 197431
                    },
                    {
                      "name": 30037
                    },
                    {
                      "name": 130973
                    },
                    {
                      "name": 24838
                    },
                    {
                      "name": 264953
                    },
                    {
                      "name": 50887
                    },
                    {
                      "name": 72073
                    },
                    {
                      "name": 6503
                    },
                    {
                      "name": 89871
                    },
                    {
                      "name": 252832
                    },
                    {
                      "name": 97174
                    },
                    {
                      "name": 36947
                    },
                    {
                      "name": 104027
                    },
                    {
                      "name": 26571
                    },
                    {
                      "name": 220809
                    },
                    {
                      "name": 105313
                    },
                    {
                      "name": 98980
                    },
                    {
                      "name": 244752
                    },
                    {
                      "name": 80784
                    },
                    {
                      "name": 22678
                    },
                    {
                      "name": 14700
                    },
                    {
                      "name": 233021
                    },
                    {
                      "name": 53776
                    },
                    {
                      "name": 267262
                    },
                    {
                      "name": 240257
                    },
                    {
                      "name": 138792
                    },
                    {
                      "name": 98597
                    },
                    {
                      "name": 131780
                    },
                    {
                      "name": 239770
                    },
                    {
                      "name": 93621
                    },
                    {
                      "name": 28074
                    },
                    {
                      "name": 52604
                    },
                    {
                      "name": 166255
                    },
                    {
                      "name": 180472
                    },
                    {
                      "name": 210061
                    },
                    {
                      "name": 201722
                    },
                    {
                      "name": 44384
                    },
                    {
                      "name": 38776
                    },
                    {
                      "name": 251232
                    },
                    {
                      "name": 121844
                    },
                    {
                      "name": 93635
                    },
                    {
                      "name": 255510
                    },
                    {
                      "name": 150703
                    },
                    {
                      "name": 1865
                    },
                    {
                      "name": 244458
                    },
                    {
                      "name": 74917
                    },
                    {
                      "name": 217977
                    },
                    {
                      "name": 7369
                    },
                    {
                      "name": 30343
                    },
                    {
                      "name": 25200
                    },
                    {
                      "name": 33131
                    },
                    {
                      "name": 176168
                    },
                    {
                      "name": 200960
                    },
                    {
                      "name": 196773
                    },
                    {
                      "name": 153667
                    },
                    {
                      "name": 139507
                    },
                    {
                      "name": 47975
                    },
                    {
                      "name": 244555
                    },
                    {
                      "name": 69761
                    }
                  ]
                },
                {
                  "name": 197285,
                  "children": [
                    {
                      "name": 79586
                    }
                  ]
                },
                {
                  "name": 144746
                },
                {
                  "name": 87045
                },
                {
                  "name": 42609
                },
                {
                  "name": 230633
                },
                {
                  "name": 240909,
                  "children": [
                    {
                      "name": 110604
                    },
                    {
                      "name": 58992
                    },
                    {
                      "name": 83609
                    },
                    {
                      "name": 110540
                    },
                    {
                      "name": 98756
                    },
                    {
                      "name": 105452
                    },
                    {
                      "name": 81033
                    },
                    {
                      "name": 149324
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "name": 190184,
          "children": [
            {
              "name": 5993
            }
          ]
        },
        {
          "name": 72294,
          "children": [
            {
              "name": 139478,
              "children": [
                {
                  "name": 126700
                },
                {
                  "name": 142192
                },
                {
                  "name": 84169
                }
              ]
            },
            {
              "name": 246415,
              "children": [
                {
                  "name": 128108
                },
                {
                  "name": 214511
                },
                {
                  "name": 5079
                }
              ]
            },
            {
              "name": 241841
            },
            {
              "name": 67505,
              "children": [
                {
                  "name": 11156
                }
              ]
            },
            {
              "name": 72717
            },
            {
              "name": 256240,
              "children": [
                {
                  "name": 179594
                },
                {
                  "name": 133891
                },
                {
                  "name": 109429
                },
                {
                  "name": 147216
                },
                {
                  "name": 115147
                },
                {
                  "name": 181733
                }
              ]
            },
            {
              "name": 16557,
              "children": [
                {
                  "name": 123283
                },
                {
                  "name": 204640
                },
                {
                  "name": 76209
                },
                {
                  "name": 145710
                }
              ]
            },
            {
              "name": 205129
            },
            {
              "name": 142064
            },
            {
              "name": 186747
            },
            {
              "name": 249327,
              "children": [
                {
                  "name": 194169
                },
                {
                  "name": 219025
                },
                {
                  "name": 201033
                },
                {
                  "name": 205048
                }
              ]
            },
            {
              "name": 114054
            },
            {
              "name": 21583
            },
            {
              "name": 122080
            }
          ]
        },
        {
          "name": 59853,
          "children": [
            {
              "name": 72016
            },
            {
              "name": 127637
            },
            {
              "name": 60592,
              "children": [
                {
                  "name": 147091
                },
                {
                  "name": 5476
                },
                {
                  "name": 152933
                },
                {
                  "name": 158332
                },
                {
                  "name": 36591
                },
                {
                  "name": 57629
                }
              ]
            },
            {
              "name": 228003
            },
            {
              "name": 140924
            },
            {
              "name": 222069
            },
            {
              "name": 120695
            },
            {
              "name": 201899
            },
            {
              "name": 126959
            },
            {
              "name": 171318
            },
            {
              "name": 134393
            },
            {
              "name": 24393
            },
            {
              "name": 77832
            },
            {
              "name": 52320,
              "children": [
                {
                  "name": 117052
                },
                {
                  "name": 65806
                },
                {
                  "name": 221960
                },
                {
                  "name": 38166
                },
                {
                  "name": 144969
                }
              ]
            }
          ]
        }
      ]
    }
  ]
};

// Set the dimensions and margins of the diagram
var margin = {top: 20, right: 90, bottom: 30, left: 90},
  width = 960 - margin.left - margin.right,
  height = 900 - margin.top - margin.bottom;

// append the svg object to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body").append("svg")
  .attr("width", width + margin.right + margin.left)
  .attr("height", height + margin.top + margin.bottom)
  .call(
    d3.zoom().on("zoom", function() {
        svg.attr("transform", d3.event.transform); 
    })
  )
  .append("g")
  .attr("transform", "translate("
        + margin.left + "," + margin.top + ")");
  var i = 0,
  duration = 750,
  root;

// declares a tree layout and assigns the size
var treemap = d3.tree().size([height, width]);

// Assigns parent, children, height, depth
root = d3.hierarchy(treeData, function(d) { return d.children; });
root.x0 = height / 2;
root.y0 = 0;

// Collapse after the second level
root.children.forEach(collapse);

update(root);

// Collapse the node and all it's children
function collapse(d) {
if(d.children) {
  d._children = d.children
  d._children.forEach(collapse)
  d.children = null
}
}

function update(source) {

// Assigns the x and y position for the nodes
var treeData = treemap(root);

// Compute the new tree layout.
var nodes = treeData.descendants(),
    links = treeData.descendants().slice(1);

// Normalize for fixed-depth.
nodes.forEach(function(d){ d.y = d.depth * 180});

// ****************** Nodes section ***************************

// Update the nodes...
var node = svg.selectAll('g.node')
    .data(nodes, function(d) {return d.id || (d.id = ++i); });

// Enter any new modes at the parent's previous position.
var nodeEnter = node.enter().append('g')
    .attr('class', 'node')
    .attr("transform", function(d) {
      return "translate(" + source.y0 + "," + source.x0 + ")";
  })
  .on('click', click);

// Add Circle for the nodes
nodeEnter.append('circle')
    .attr('class', 'node')
    .attr('r', 1e-6)
    .style("fill", function(d) {
        return d._children ? "lightsteelblue" : "#fff";
    });

// Add labels for the nodes
nodeEnter.append('text')
    .attr("dy", ".35em")
    .attr("x", function(d) {
        return d.children || d._children ? -13 : 13;
    })
    .attr("text-anchor", function(d) {
        return d.children || d._children ? "end" : "start";
    })
    .text(function(d) { return d.data.name; });

// UPDATE
var nodeUpdate = nodeEnter.merge(node);

// Transition to the proper position for the node
nodeUpdate.transition()
  .duration(duration)
  .attr("transform", function(d) { 
      return "translate(" + d.y + "," + d.x + ")";
   });

// Update the node attributes and style
// Highlight pathway between two nodes 
nodeUpdate.select('circle.node') 
  .attr('r', 4.5)
  .style("fill", function(d) {
    if(d.data.class === "selected") {  
      return "#ff0"; //yellow
    } 
    if (d.data.class === "found"){
      //show pathway of hidden nodes 
      showHidden(d); 
      return "#ff4136"; //red
    }
    else if(d._children){
      return "lightsteelblue"; 
    } 
    else{
      return "#fff";
    }
  })
  .style("stroke", function(d) {  
    if (d.data.class === "selected") {
      return "#ff0"; 
    }
    if(d.class === "found"){
      return "#ff4136"; 
    } 
  })
  .attr('cursor', 'pointer');


// Remove any exiting nodes
var nodeExit = node.exit().transition()
    .duration(duration)
    .attr("transform", function(d) {
        return "translate(" + source.y + "," + source.x + ")";
    })
    .remove();

// On exit reduce the node circles size to 0
nodeExit.select('circle')
  .attr('r', 1e-6);

// On exit reduce the opacity of text labels
nodeExit.select('text')
  .style('fill-opacity', 1e-6);

// ****************** links section ***************************

// Update the links...
var link = svg.selectAll('path.link')
    .data(links, function(d) { return d.id; });
   

// Enter any new links at the parent's previous position.
var linkEnter = link.enter().insert('path', "g")
    .attr("class", "link")
    .attr('d', function(d){
      var o = {x: source.x0, y: source.y0}
      return diagonal(o, o)
    });

// UPDATE
var linkUpdate = linkEnter.merge(link); /** Link gets called when it is being drawn */

// Transition back to the parent element position
linkUpdate.transition()
    .duration(duration)
    .attr('d', function(d){ return diagonal(d, d.parent) })
    .style("stroke", (d) => {
      if (d.data.class === "found") {
        return "#ff4136"; //red
      }
    });

// Remove any exiting links
var linkExit = link.exit().transition()
    .duration(duration)
    .attr('d', function(d) {
      var o = {x: source.x, y: source.y}
      return diagonal(o, o)
    })
    .remove();

// Store the old positions for transition.
nodes.forEach(function(d){
  d.x0 = d.x;
  d.y0 = d.y;
});

// Creates a curved (diagonal) path from parent to the child nodes
function diagonal(s, d) {

  path = `M ${s.y} ${s.x}
          C ${(s.y + d.y) / 2} ${s.x},
            ${(s.y + d.y) / 2} ${d.x},
            ${d.y} ${d.x}`

  return path
}

// Toggle children on click. - maybe beed to also put ifFound()
function click(d) {
  if (d.children) {
      d._children = d.children;
      d.children = null;
    } else {
      d.children = d._children;
      d._children = null;
    }
  update(d);
}


function showHidden(d) {
    //if this node has hidden children 
    if (d._children) {
        d.children = d._children; 
        d._children = null; 
    }
}
} //end of update function


/*Traverses through tree to find correct path between
two nodes*/
function buildPathFrom(node, dest, path) {
  if(node.name === dest) { 
    //node is equal to dest 
    path.push(node);
    return path; 
  } else if (node.children || node._children) { 
    //Not the node we want but has children 
    let children = (node.children) ? node.children : node._children; 
    for (let i = 0; i < children.length; i++) {
      path.push(children[i]); 
      let found = buildPathFrom(children[i], dest, path); 
      if (found) {
        return path; 
      } else {
        path.pop(); 
      }
    }
  } else {
     //At the end of the branch and node was not found
    return false; 
  }
}

//return the path 
function getPath(start, end, tree) {
  let path = buildPathFrom(tree, end, []);  
  return path; 
}

//checks root 
function isRoot (node) {
  return node.name === "1"; 
}

//if node is in path label it as found
function markAsFound(node) {
  node.class = "found"; 
}

function expandChildren(node) { //need to work on! 
  if (node._children) {
    node.children = node._children; 
    node._children = null; 
  }
}

//highlights path
function highlightPath (path) {
  for (const node of path) {
    if (!isRoot(node)) {
      markAsFound(node); 
      expandChildren(node); 
      update(node); 
    }
  }
}

//Selects node, when user enters in text box 1
let selectedUser1; 
$("#user_1").on("input", () => {
  let search = $("#user_1").val();
  search = parseInt(search);  
  console.log("search:", search); 
  if (search) {
    let currentNode = findNode(search, treeData); 
    console.log("currentnode", currentNode);
    if (currentNode === null) {
      return; 
    } 
    if (selectedUser1 && currentNode !== selectedUser1) {
      deselect(selectedUser1); 
      select(currentNode); 
      selectedUser1 = currentNode; 
    } else {
      select(currentNode); 
      selectedUser1 = currentNode; 
    }
  }
});

//Selects node, when user enters in text box 2 
let selectedUser2; 
$("#user_2").on("input", () => {
  let search = $("#user_2").val();
  search = parseInt(search);  
  console.log("search2:", search); 
  if (search) {
    let currentNode = findNode(search, treeData); 
    console.log("currentnode", currentNode);
    if (currentNode === null) {
      return; 
    } 
    if (selectedUser2 && currentNode !== selectedUser2) {
      deselect(selectedUser2); 
      select(currentNode); 
      selectedUser2 = currentNode; 
    } else {
      select(currentNode); 
      selectedUser2 = currentNode; 
    }
  }
});

//Returns user's input (target) if found in tree 
function findNode(target, currentNode) {
  //if target is the current node return it 
  if (target == currentNode.name) {
    return currentNode; 
  } else if ((children = getChildren(currentNode))) {
    // for each node's children 
    for (const child of children) {
      //if the target is equal to found return it 
      if ((found = findNode(target, child))){
        return found; 
      }
    }
  } else { 
    //return null because it is not in the tree 
    return null; 
  }
}

//Returns children of node if node has any 
function getChildren(node) {  
  return node.children || node._children; 
}

//Labels the node as selected if highlighted
function select(node) {
  node.class = "selected"; 
  update(node); 
}

//Labels the node as deselected to un-highlight 
function deselect(node) {
  node.class = ""; 
  update(node); 
}

/*when button is clicked on, highlight path between
  the two inputs 
*/
$( "#btnsearchPath" ).click(() => {
  let user1 = $("#user_1").val(); 
  console.log("User 1: " + user1); 
  let user2 = $("#user_2").val(); 
  console.log("User 2: " + user2); 

  user1 = parseInt(user1); 
  user2 = parseInt(user2);

  if(!user1 || !user2) {
    alert("Please enter 2 users!")
  }

  let path = getPath(user1, user2, treeData); 
  highlightPath(path); 
  console.log(path); 
  console.log(findNode("1", treeData)); 
})


