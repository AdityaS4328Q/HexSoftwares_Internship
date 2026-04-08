from urllib import response
import streamlit as st
from googleapiclient.discovery import build
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="YouTube Dashboard", layout="wide")
st.title("My YouTube Data Dashboard 📺")

if "data_fetched" not in st.session_state:
    st.session_state.data_fetched = False

st.sidebar.header("API Settings")
api_key = st.sidebar.text_input("Enter your YouTube API Key", type="password") 
channel_id = st.sidebar.text_input("Enter Channel ID", value="UCX6OQ3DkcsbYNE6H8uQQuVA") 
num_videos = st.sidebar.slider("Number of Recent Videos to Analyze", min_value=5, max_value=50, value=10)

if st.sidebar.button("Fetch Channel Data"):
    if not api_key:
        st.error("⚠️ Please enter your API Key in the sidebar first!")
    else:
        st.session_state.data_fetched = True

if st.session_state.data_fetched and api_key:
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        request = youtube.channels().list(
            part="snippet,statistics,contentDetails",
            id=channel_id
        )
        response = request.execute()
        
        if 'items' in response:
            channel_data = response['items'][0]
            snippet = channel_data['snippet']
            stats = channel_data['statistics']
            uploads_playlist_id = channel_data['contentDetails']['relatedPlaylists']['uploads']
            
            st.subheader(f"Channel: {snippet['title']}")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Subscribers", f"{int(stats['subscriberCount']):,}")
            col2.metric("Total Views", f"{int(stats['viewCount']):,}")
            col3.metric("Total Videos", f"{int(stats['videoCount']):,}")
            
            st.markdown("---")
            st.subheader("📊 Recent Video Performance")
            
            playlist_req = youtube.playlistItems().list(
                part="snippet",
                playlistId=uploads_playlist_id,
                maxResults=num_videos
            )
            playlist_resp = playlist_req.execute()
            
            video_ids = []
            for item in playlist_resp['items']:
                video_ids.append(item['snippet']['resourceId']['videoId'])
            
            video_req = youtube.videos().list(
                part="snippet,statistics",
                id=','.join(video_ids)
            )
            video_resp = video_req.execute()
            
            video_data = []
            for video in video_resp['items']:
                title = video['snippet']['title']
                views = int(video['statistics'].get('viewCount', 0))
                likes = int(video['statistics'].get('likeCount', 0))
                
                video_data.append({
                    'Title': title,
                    'Views': views,
                    'Likes': likes
                })
                
            df = pd.DataFrame(video_data)
            sort_by = st.selectbox("Sort videos by:", ["Views", "Likes"])
            df_sorted = df.sort_values(by=sort_by, ascending=False)
            
            fig = px.bar(df_sorted, x='Title', y=sort_by, 
                         title=f"Top {num_videos} Recent Videos (Sorted by {sort_by})",
                         color=sort_by, color_continuous_scale='Blues' if sort_by == 'Likes' else 'Reds',
                         hover_data=['Views', 'Likes'])
            
            fig.update_xaxes(showticklabels=False) 
            st.plotly_chart(fig, use_container_width=True)
            
            with st.expander("Show Raw Video Data"):
                st.dataframe(df_sorted)

        else:
            st.error("Channel not found. Please check the Channel ID.")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("👈 Enter your API Key in the sidebar and click 'Fetch Channel Data' to start!")