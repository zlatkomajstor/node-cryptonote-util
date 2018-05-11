{
    "targets": [
        {
            "target_name": "cryptonote",
            "sources": [
                "src/main.cc",
                "src/cryptonote_core/cryptonote_format_utils.cpp",
                "src/crypto/tree-hash.c",
                "src/crypto/crypto.cpp",
                "src/crypto/crypto-ops.c",
                "src/crypto/crypto-ops-data.c",
                "src/crypto/hash.c",
                "src/crypto/keccak.c",
                "src/crypto/keccak.c",
				"src/crypto/cn_slow_hash_hard_intel.cpp",
                "src/crypto/cn_slow_hash_soft.cpp",
                "src/crypto/cn_slow_hash.hpp",
                "src/common/base58.cpp",
            ],
            "include_dirs": [
                "src",
                "src/contrib/epee/include",
            ],
            "link_settings": {
                "libraries": [
                    "-lboost_system",
                    "-lboost_date_time",
                ]
            },
            "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ],
            "cflags_cc": [
                  "-std=c++11",
                  "-fexceptions",
                  "-frtti",
            ],
        }
    ]
}
