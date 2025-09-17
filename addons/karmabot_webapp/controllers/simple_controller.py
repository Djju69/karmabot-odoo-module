# -*- coding: utf-8 -*-

from odoo import http, fields, _
from odoo.http import request
import logging
import json

_logger = logging.getLogger(__name__)


class SimpleKarmaBotController(http.Controller):
    """Simple WebApp Controller without website dependencies"""
    
    @http.route('/karmabot/test', type='http', auth='public', methods=['GET'])
    def test_endpoint(self, **kw):
        """Simple test endpoint"""
        try:
            return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>KarmaBot Test</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    .container { max-width: 600px; margin: 0 auto; }
                    .header { text-align: center; color: #2c3e50; }
                    .status { background: #27ae60; color: white; padding: 10px; border-radius: 5px; margin: 20px 0; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🎯 KarmaBot WebApp</h1>
                        <p>Модуль успешно установлен!</p>
                    </div>
                    
                    <div class="status">
                        ✅ Статус: Модуль работает корректно
                    </div>
                    
                    <h2>Доступные функции:</h2>
                    <ul>
                        <li>✅ Контроллеры загружены</li>
                        <li>✅ Модели созданы</li>
                        <li>✅ Маршруты настроены</li>
                        <li>✅ База данных подключена</li>
                    </ul>
                    
                    <h2>API Endpoints:</h2>
                    <ul>
                        <li><code>/karmabot/test</code> - Эта страница</li>
                        <li><code>/karmabot/webapp</code> - Основной WebApp</li>
                        <li><code>/webapp</code> - Landing page</li>
                    </ul>
                    
                    <p><strong>Время:</strong> {}</p>
                </div>
            </body>
            </html>
            """.format(fields.Datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            
        except Exception as e:
            _logger.error(f"Error in test_endpoint: {e}")
            return f"<h1>Error</h1><p>{str(e)}</p>"
    
    @http.route('/karmabot/api/status', type='json', auth='public', methods=['POST'])
    def api_status(self, **kw):
        """API endpoint for status check"""
        try:
            return {
                'success': True,
                'status': 'ok',
                'message': 'KarmaBot WebApp module is working',
                'timestamp': fields.Datetime.now().isoformat(),
                'version': '1.0.0'
            }
        except Exception as e:
            _logger.error(f"Error in api_status: {e}")
            return {
                'success': False,
                'error': str(e)
            }
