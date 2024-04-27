const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.post('/create-project', async (req, res) => {
    try {
        const response = await axios.post('https://gitlab.example.com/api/v4/projects', {
            name: req.body.projectName,
            namespace_id: req.body.namespaceId // フォームからのデフォルト値またはユーザー入力値を使用
        }, {
            headers: {'PRIVATE-TOKEN': process.env.PRIVATE_TOKEN}
        });
        res.send(`Project created successfully: ${response.data.web_url}`);
    } catch (error) {
        res.status(500).send(`Error creating project: ${error.message}`);
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
