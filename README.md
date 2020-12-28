# 2020年 ロボットシステム学 課題2


## 目標

- ROS2で短い小説を読んでもらう。

## 概要

- ROS2を用いてパブリッシャとサブスクライバーの関係を活用する。

## 動作環境

- Ubuntu 18.04
- ROS2
    
## 内容

- このリポジトリのものはROS2が設置されている前提である。
- talkerはパブリッシャーであり、無限ループとして数字を増やしながらパブリッシングする。
- readerはサブスクライバーであり、パブリッシャーからもらったトピックに当たるものを画面に流す。
- ローンチファイルでパブリッシャーとサブスクライバーを一気に実行させる。
- 秒ごとに小説を１行目ずつ見せる。

## インストール手順

1. git cloneでこのリポジトリをros2_ws/srcの下にコピーペーストする。
2. sudo rosdep install -i --from-path src --rosdistro foxy -yを実行する。
2. ~/ros2_ws/のディレクトリに戻り、colcon buildを実行する。
3. source install/setup.bashとsource install/local_setup.bashを実行してパスを通す。
4. ros2 launch mypkg talk_read.launch.pyを実行する。


## 実行例

- [動画リンク](https://youtu.be/7FpO0fsVnIg)

## ライセンス

- [BSD 3-Clause License](https://github.com/Keozgb/mypkg_ros2project/blob/main/LICENSE)
